# Errynie Cyril – Operations & Data Portfolio

![Excel Badge](https://img.shields.io/badge/Excel-Dashboard-green) ![SQL Badge](https://img.shields.io/badge/SQL-DataAnalysis-blue) ![Python Badge](https://img.shields.io/badge/Python-Basic-yellow) ![Power BI Badge](https://img.shields.io/badge/PowerBI-Foundational-orange)

Operations and data professional with **2+ years of experience** in high-volume data management, reporting, and operational support. Skilled in **dashboards**, **SQL analytics**, **data validation**, and **workflow optimization**. This portfolio demonstrates how I **tackle data challenges, implement solutions, and deliver measurable impact**.

## Skills & Tools
**Excel:** Pivot Tables, Power Query, Dashboards, Data Visualization  
**SQL:** Data Analysis, Aggregation, Validation  
**Python:** Basic data aggregation & analysis  
**Power BI:** Foundational  
Data Cleaning & Validation  
Workflow Coordination & KPI Tracking  
Tools: Swing/D365, OnBase, Kofax (familiarity)

## Featured Project: Order & Transaction Tracking Dashboard (Excel + SQL)
**Problem:** Manual tracking of **1,500+ transactions** was slow, error-prone, and made KPI tracking difficult.

**Solution:** Built Excel dashboards with Pivot Tables and interactive visuals, used SQL queries to **clean, validate, and aggregate data**, and structured reports to ensure **accurate, actionable insights**.

**Impact:** Reduced manual reporting effort by **20%**, increased visibility of product and team performance, ensured reliable, accurate data for decision-making.

**Before → After:**  
- *Manual tracking* → **Automated dashboards**  
- *Slow trend analysis* → **Instant insights**  
- *Risk of errors* → **Reliable KPIs**

**Tools Used:** Excel, SQL

**Dashboard Preview:** ![Dashboard Preview](dashboard-preview.png)

## SQL Work Examples

**Query 1: Revenue by Product Category**  
`SELECT product_category, SUM(revenue) AS total_revenue, AVG(revenue) AS avg_revenue FROM sales_data WHERE order_date >= '2023-01-01' GROUP BY product_category ORDER BY total_revenue DESC;`  
*Aggregates total & average revenue by category, ranks categories.*

**Query 2: Top Performing Products**  
`SELECT product_name, SUM(revenue) AS total_revenue FROM sales_data GROUP BY product_name ORDER BY total_revenue DESC;`  
*Highlights high-performing products.*

**Query 3: Data Validation Check**  
`SELECT COUNT(*) AS total_records, COUNT(DISTINCT order_id) AS unique_orders FROM sales_data;`  
*Checks for duplicates and validates dataset.*

**Concepts Applied:** Aggregation (`SUM`, `AVG`), `GROUP BY`, filtering (`WHERE`), sorting (`ORDER BY`), data validation techniques

## What I Do
- Build dashboards to improve reporting visibility  
- Clean and validate data for operational accuracy  
- Support operations and reporting with structured analysis

## Contact
- Email: **erryniec26@gmail.com**  
- Location: **Malaysia**  
- GitHub: [ErrynieCyril Portfolio](https://github.com/erryniec26)
