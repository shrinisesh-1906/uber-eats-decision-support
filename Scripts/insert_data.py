import pandas as pd
import sqlite3


# Load cleaned data
df = pd.read_csv('data/cleaned_restaurants.csv')

# Connect to database
conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

# Insert data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO restaurants
        (name, location, cuisines, rating, cost, online_order, book_table, price_category)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row['name'],
        row['location'],
        row['cuisines'],
        row['rate'],
        row['approx_cost_for_two'],
        row['online_order'],
        row['book_table'],
        row['price_category']
    ))

conn.commit()
conn.close()

print("✅ Data inserted successfully!")