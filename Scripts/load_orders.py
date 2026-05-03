import pandas as pd
import sqlite3
import json

# Load JSON
with open('data/orders (1).json') as f:
    data = json.load(f)

# Handle different JSON formats
if isinstance(data, dict):
    # If JSON is wrapped like {"orders": [...]}
    data = data.get('orders', list(data.values())[0])

# Convert to DataFrame
df = pd.DataFrame(data)

print("Loaded JSON")
print("Columns:", df.columns)

# Connect DB
conn = sqlite3.connect('database/database.db')

# Save to SQL
df.to_sql('orders', conn, if_exists='replace', index=False)

print("Orders table created successfully!")