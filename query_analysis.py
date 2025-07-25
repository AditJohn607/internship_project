import sqlite3
import pandas as pd

conn = sqlite3.connect('ecommerce_returns.db')

query1 = """
SELECT 
    COUNT(*) AS total_orders,
    SUM(CASE WHEN return_status = 'Returned' THEN 1 ELSE 0 END) AS total_returns
FROM returns_data;
""" 
print("\n1. Total Orders and Returns:\n", df1) 

query2 = """
SELECT 
    product_category,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN return_status = 'Returned' THEN 1 ELSE 0 END) AS total_returns,
    ROUND(100.0 * SUM(CASE WHEN return_status = 'Returned' THEN 1 ELSE 0 END) / COUNT(*), 2) AS return_rate_percentage
FROM returns_data
GROUP BY product_category
ORDER BY return_rate_percentage DESC;
"""
df2 = pd.read_sql_query(query2, conn)
print("\n2. Return Rate by Product Category:\n", df2)

query3 = """
SELECT 
    shipping_method,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN return_status = 'Returned' THEN 1 ELSE 0 END) AS total_returns,
    ROUND(100.0 * SUM(CASE WHEN return_status = 'Returned' THEN 1 ELSE 0 END) / COUNT(*), 2) AS return_rate_percentage
FROM returns_data
GROUP BY shipping_method
ORDER BY return_rate_percentage DESC;
"""
df3 = pd.read_sql_query(query3, conn)
print("\n3. Return Rate by Shipping Method:\n", df3)

query4 = """
SELECT 
    payment_method,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN return_status = 'Returned' THEN 1 ELSE 0 END) AS total_returns,
    ROUND(100.0 * SUM(CASE WHEN return_status = 'Returned' THEN 1 ELSE 0 END) / COUNT(*), 2) AS return_rate_percentage
FROM returns_data
GROUP BY payment_method
ORDER BY return_rate_percentage DESC;
"""
df4 = pd.read_sql_query(query4, conn)
print("\n4. Return Rate by Payment Method:\n", df4)

query5 = """
SELECT 
    product_category,
    AVG(days_to_return) AS avg_days_to_return
FROM returns_data
WHERE return_status = 'Returned'
GROUP BY product_category
ORDER BY avg_days_to_return DESC;
"""
df5 = pd.read_sql_query(query5, conn)
print("\n5. Average Days to Return by Product Category:\n", df5)

conn.close()