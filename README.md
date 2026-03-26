# Errynie Cyril | Operations & Data Portfolio
[![Excel](https://img.shields.io/badge/Excel-Dashboards%20%26%20VBA-green)](https://github.com/erryniec26)
[![SQL](https://img.shields.io/badge/SQL-Data%20Analytics-blue)](https://github.com/erryniec26)
[![Python](https://img.shields.io/badge/Python-Data%20Cleaning-yellow)](https://github.com/erryniec26)
[![Power BI](https://img.shields.io/badge/Power%20BI-Foundational-orange)](https://github.com/erryniec26)

Operations and Data professional with **2+ years of experience** managing high-volume data environments (1,500+ transactions). I specialize in bridging the gap between raw data and business decisions through **automated reporting, SQL validation, and workflow optimization.**

---

## 🛠️ Technical Stack
* **Data Analysis:** SQL (PostgreSQL/MySQL), Excel (Power Query, Pivot Tables, Advanced Formulas)
* **Visualization:** Interactive Excel Dashboards, Power BI (Foundational)
* **Operations:** Workflow Logic, KPI Tracking, Data Integrity & Validation
* **Tools:** ERP Systems (D365/Swing), Document Management (OnBase, Kofax)

---

## 🚀 Featured Projects

### 1. Sales Performance & Operations Dashboard (Excel + SQL)
**Objective:** Replace an error-prone manual tracking process for RM16M in revenue and 1,500+ annual transactions.

* **The Problem:** Manual reporting took 4+ hours per week and lacked real-time KPI visibility.
* **The Solution:** Built a dynamic dashboard using **Power Query** for data cleaning and **Slicers** for interactive filtering.
* **Impact:** Reduced manual reporting time by **20%** and provided instant visibility into top-performing products.

### 2. Medical Appointment Workflow Logic
**Objective:** Designed a structured logic flow for a digital appointment management system.
* **Scope:** Mapped the end-to-end journey from user authentication to automated report generation.
* **Outcome:** Created a clear technical blueprint for developers to ensure seamless patient-doctor scheduling.

---

## 💻 SQL Portfolio Examples

### 1. Revenue Segmentation & Ranking
*Business Goal: Identify high-value categories for targeted marketing.*
```sql
SELECT 
    product_category, 
    SUM(revenue) AS total_revenue, 
    AVG(revenue) AS avg_order_value 
FROM sales_data 
WHERE order_date >= '2025-01-01' 
GROUP BY product_category 
ORDER BY total_revenue DESC;

2. Data Integrity Check (Audit)
Business Goal: Ensure 100% data accuracy before stakeholder reporting.
SELECT 
    COUNT(*) AS total_records, 
    COUNT(DISTINCT order_id) AS unique_orders,
    (COUNT(*) - COUNT(DISTINCT order_id)) AS duplicate_count
FROM sales_data;

🎯 Career Focus
I am currently transitioning into IT and Business Analysis roles. My focus is on leveraging my background in operations to help organizations streamline data workflows and implement scalable technical solutions.
📬 Contact Information
 * Location: Malaysia
 * Email: erryniec26@gmail.com
 * GitHub: erryniec26
