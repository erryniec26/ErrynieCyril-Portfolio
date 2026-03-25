# Errynie Cyril – Data & Operations Portfolio

Data and operations professional focused on building **reporting systems, dashboards, and data validation workflows** using Excel and SQL.

Experienced in handling high-volume data and improving reporting efficiency through structured analysis and visualization.

---

## 🔧 Skills & Tools

* **Excel** (Dashboards, Pivot Tables, Data Visualization)
* **SQL** (Data Analysis, Aggregation, Validation)
* **Power BI** (Foundational)
* Data Cleaning & Process Improvement

---

## 📊 Featured Project

### Sales & Transaction Analysis Dashboard (Excel + SQL)

#### Overview

Developed a reporting system to analyze transaction data and track key business metrics, including revenue, product performance, and sales trends.

---

#### Business Problem

Manual tracking of transaction data made it difficult to:

* Monitor revenue performance efficiently
* Identify top-performing products
* Ensure data accuracy across records

---

#### Solution

Built an Excel-based dashboard supported by SQL data validation to streamline reporting and improve data reliability.

---

#### Key Contributions

* Cleaned and structured a dataset of **1,500+ transactions**
* Built an interactive Excel dashboard using **Pivot Tables and visualization**
* Used SQL queries to generate insights and validate data
* Organized structured data for efficient reporting

---

#### Impact

* Improved visibility of revenue and performance trends
* Reduced manual tracking effort
* Increased data accuracy and reliability

---

#### Tools Used

* Excel
* SQL

---

#### Dashboard Preview

![Dashboard Preview](dashboard-preview.png)

---

## 📊 SQL Analysis & Data Validation

Used SQL queries to analyze transaction data, validate accuracy, and generate business insights for reporting.

---

### Query 1: Revenue by Product Category

```sql
SELECT product_category,
       SUM(revenue) AS total_revenue,
       AVG(revenue) AS avg_revenue
FROM sales_data
WHERE order_date >= '2023-01-01'
GROUP BY product_category
ORDER BY total_revenue DESC;
```

**What this query does:**

* Calculates total and average revenue by product category
* Filters transaction data
* Ranks categories by highest revenue

---

### Query 2: Top Performing Products

```sql
SELECT product_name,
       SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY product_name
ORDER BY total_revenue DESC;
```

**What this query does:**

* Identifies top-performing products based on revenue
* Helps highlight best-selling items

---

### Query 3: Data Validation Check

```sql
SELECT COUNT(*) AS total_records,
       COUNT(DISTINCT order_id) AS unique_orders
FROM sales_data;
```

**What this query does:**

* Checks for duplicate or inconsistent records
* Ensures data accuracy before analysis

---

### SQL Concepts Applied

* Data aggregation (SUM, AVG)
* Data grouping (GROUP BY)
* Filtering (WHERE)
* Sorting (ORDER BY)
* Data validation techniques

---

## 📁 Project Files

* Excel Dashboard
* SQL Queries
* Supporting Documentation (PDF)

---

## 📌 What I Do

* Build dashboards to improve reporting visibility
* Clean and validate data for accuracy
* Support operations through structured data analysis

---

## 📫 Contact

* Email: [erryniec26@gmail.com](mailto:erryniec26@gmail.com)
* Location: Malaysia
* GitHub: https://github.com/erryniec26
