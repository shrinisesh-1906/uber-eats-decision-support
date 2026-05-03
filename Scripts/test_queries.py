import sqlite3
import pandas as pd
import queries

conn = sqlite3.connect('database/database.db')

df = pd.read_sql(queries.TOP_LOCATIONS, conn)

print(df.head())