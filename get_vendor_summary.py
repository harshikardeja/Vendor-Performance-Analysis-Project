import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

# Set up logging
logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def create_vendor_summary(conn):
    '''Merges different tables to generate overall vendor summary'''
    query = """
    WITH FreightSummary AS (
        SELECT VendorNumber, SUM(freight) AS FreightCost
        FROM vendor_invoice 
        GROUP BY VendorNumber
    ),
    PurchaseSummary AS (
        SELECT
            P.VendorNumber,
            P.VendorName,
            P.Brand,
            P.Description,
            P.PurchasePrice,
            PP.price AS ActualPrice,
            PP.Volume,
            SUM(P.Quantity) AS TotalPurchaseQuantity,
            SUM(P.Dollars) AS TotalPurchaseDollars
        FROM purchases P
        JOIN purchase_prices PP ON P.brand = PP.brand
        WHERE P.PurchasePrice > 0
        GROUP BY P.VendorNumber, P.VendorName, P.Brand, P.Description, P.PurchasePrice, PP.price, PP.Volume
    ),
    SalesSummary AS (
        SELECT
            VendorNo AS VendorNumber,
            Brand,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    )
    SELECT    
        PS.VendorNumber,
        PS.VendorName,
        PS.Brand,
        PS.Description,
        PS.PurchasePrice,
        PS.ActualPrice,
        PS.Volume,
        PS.TotalPurchaseQuantity,
        PS.TotalPurchaseDollars,
        SS.TotalSalesQuantity,
        SS.TotalSalesDollars,
        SS.TotalSalesPrice, 
        SS.TotalExciseTax,
        FS.FreightCost
    FROM PurchaseSummary PS
    LEFT JOIN SalesSummary SS ON PS.VendorNumber = SS.VendorNumber AND PS.Brand = SS.Brand
    LEFT JOIN FreightSummary FS ON PS.VendorNumber = FS.VendorNumber
    ORDER BY TotalSalesDollars DESC
    """
    vendor_sales_summary = pd.read_sql_query(query, conn)
    return vendor_sales_summary

def clean_data(df):
    '''Cleans and enhances the vendor summary dataframe'''
    
    df['Volume'] = df['Volume'].astype(float)

    # Fill missing values with 0
    df.fillna(0, inplace=True)

    # Clean string fields
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    # New calculated columns
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars']) * 100
    df['StockTurnOver'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalestoPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']

    return df

if __name__ == '__main__':
    # Create DB connection
    conn = sqlite3.connect('inventory.db')

    logging.info('Creating vendor summary...')
    summary_df = create_vendor_summary(conn)
    logging.info(f'Summary preview:\n{summary_df.head()}')

    logging.info('Cleaning data...')
    clean_df = clean_data(summary_df)
    logging.info(f'Cleaned data preview:\n{clean_df.head()}')

    logging.info('Ingesting data...')
    ingest_db(clean_df, 'vendor_sales_summary', conn)
    logging.info('Completed ingestion.')
