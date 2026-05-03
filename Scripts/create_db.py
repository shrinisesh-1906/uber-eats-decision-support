import sqlite3
import os
print("Current working directory:", os.getcwd())

# Connect to database (this will CREATE the file)
conn = sqlite3.connect('database/database.db')

cursor = conn.cursor()

# Create restaurants table
cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT,
    cuisines TEXT,
    rating REAL,
    cost REAL,
    online_order TEXT,
    book_table TEXT,
    price_category TEXT
)
""")

conn.commit()
conn.close()

print("✅ Database and table created successfully!")