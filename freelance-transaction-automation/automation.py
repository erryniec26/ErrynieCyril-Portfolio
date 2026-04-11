import pandas as pd
import sqlite3

# Load CSV data
df = pd.read_csv("freelance-transactions.csv")

# Clean data
df.drop_duplicates(inplace=True)
df.dropna(subset=["Revenue"], inplace=True)

# Aggregate data for dashboard
monthly_summary = df.groupby(['Product', pd.to_datetime(df['Date']).dt.to_period('M')]).agg({
    'Units Sold': 'sum',
    'Revenue': 'sum'
}).reset_index()

monthly_summary['Month'] = monthly_summary['Date'].astype(str)
monthly_summary.drop(columns=['Date'], inplace=True)

# Save cleaned CSV for dashboard
monthly_summary.to_csv("dashboard_automation_output.csv", index=False)

# Optional: Save to SQLite for demonstration
conn = sqlite3.connect("dashboard_automation.db")
monthly_summary.to_sql("monthly_summary", conn, if_exists="replace", index=False)
conn.close()

print("Automation complete: CSV and SQLite database updated.")
