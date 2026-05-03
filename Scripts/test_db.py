import sqlite3
import pandas as pd

conn = sqlite3.connect('database/database.db')

# Show all tables
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

#Try reading orders table
df_rest = pd.read_sql("SELECT * FROM restaurants LIMIT 5", conn)

print("\n✅ Restaurants Data:")
print(df_rest)

print("\nColumns:", df_rest.columns)

# -----------------------------
#  Orders Sample
# -----------------------------
df_orders = pd.read_sql("SELECT * FROM orders LIMIT 5", conn)

print("\n✅ Orders Data:")
print(df_orders)

print("\nColumns:", df_orders.columns)