# 📊 Vendor Performance Analysis Project

## 📌 Overview
The **Vendor Performance Analysis Project** is a data analytics initiative aimed at evaluating vendor efficiency, identifying top performers, and uncovering improvement opportunities.  
By analyzing purchase data, inventory turnover, and sales contributions, the project provides actionable insights to optimize vendor relationships and improve profitability.

---

## 🎯 Objectives
- Identify **underperforming vendors** based on key metrics.
- Highlight **top vendors** driving the most value.
- Analyze the **impact of bulk purchases** on profitability.
- Evaluate **inventory turnover** and stock efficiency.
- Measure **profitability variance** across vendors.

---

## 🗂 Dataset
The dataset contains vendor-level transactional and inventory data with fields such as:
- `VendorName`
- `Purchase_Contribution%`
- `StockTurnOver`
- `Profitability`
- `BulkPurchaseIndicator`
- `InventoryValue`

---

## 🔍 Key Analysis Performed
1. **Top Vendor Identification**  
   Ranking vendors by purchase contribution and profitability.
   
2. **Underperforming Vendor Detection**  
   Filtering vendors with low turnover or negative profitability trends.
   
3. **Bulk Purchase Impact**  
   Comparing profitability and stock turnover between bulk vs. non-bulk purchases.
   
4. **Inventory Efficiency**  
   Analyzing stock turnover ratios for better capital utilization.

5. **Profitability Variance**  
   Assessing fluctuation in margins to detect risk areas.

---

## 📈 Tools & Libraries Used
- **Python** – Data processing & analysis
- **Pandas** – Data manipulation
- **NumPy** – Numerical calculations
- **Matplotlib & Seaborn** – Data visualization
- **Jupyter Notebook** – Analysis workflow

---

## 📊 Sample Insights
- Vendors contributing < 2% to total purchases but with **high profitability** can be strategically scaled.
- Some high-contribution vendors have **low stock turnover**, indicating overstock or inefficiency.
- Bulk purchases may **not always lead to better margins** — analysis shows varied impact.

---

## 🖼 Visualizations
- Bar charts for **Top 10 Vendors by Purchase Contribution**
- Pie chart for **Vendor Category Share**
- Boxplots for **Stock Turnover Outlier Detection**
- Scatter plots for **Profitability vs. Contribution**
- Heatmaps for **Correlation between metrics**

