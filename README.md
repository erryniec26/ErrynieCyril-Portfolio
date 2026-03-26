## Skills & Tools

**Excel:** Pivot Tables, Power Query, Dashboards, Data Visualization

**SQL:** Data Analysis, Aggregation, Validation

**Python:** Basic data aggregation & analysis

**Power BI:** Foundational

**Data Cleaning:** Validation, Workflow Coordination, KPI Tracking

**Tools:** Swing/D365, OnBase, Kofax (familiarity)

---

## Featured Project: Sales Performance & Transaction Dashboard

**Problem:** Manual tracking of **1,500+ transactions** was slow, error-prone, and made high-level KPI tracking difficult to sustain.

**Solution:** Developed an Excel dashboard using Power Query and Pivot Tables to **clean, validate, and aggregate** complex datasets.

**Impact:** Reduced manual reporting effort by **20%**, providing stakeholders with instant visibility into team and product performance.

**Before → After:**
* *Manual tracking* → **Automated dashboards**
* *Slow trend analysis* → **Instant data insights**
* *High risk of errors* → **Reliable, validated KPIs**

---

## SQL Portfolio: Data Analysis & Validation Examples

**Query 1: Revenue by Product Category**

`SELECT product_category, SUM(revenue) AS total_revenue, AVG(revenue) AS avg_revenue FROM sales_data WHERE order_date >= '2023-01-01' GROUP BY product_category ORDER BY total_revenue DESC;`

*Aggregates total and average revenue by category to identify the highest-earning sectors.*

**Query 2: Top Performing Products**

`SELECT product_name, SUM(revenue) AS total_revenue FROM sales_data GROUP BY product_name ORDER BY total_revenue DESC;`

*Highlights top products by revenue to assist in inventory and sales strategy optimization.*

**Query 3: Data Integrity & Validation**

`SELECT COUNT(*) AS total_records, COUNT(DISTINCT order_id) AS unique_orders FROM sales_data;`

*Performs a critical audit to detect duplicates and ensure the dataset is accurate for reporting.*