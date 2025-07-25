import pandas as pd
import sqlite3
df = pd.read_csv("cleaned_ecommerce_data.csv")
conn = sqlite3.connect("ecommerce_returns.db")
df.to_sql("returns_data", conn, if_exists="replace", index=False)
rows = conn.execute("SELECT * FROM returns_data LIMIT 5;")
print("\n Sample rows from database:")
for row in rows:
    print(row)
conn.close()