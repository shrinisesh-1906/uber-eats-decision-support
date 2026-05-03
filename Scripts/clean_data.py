import pandas as pd

# Load data
df = pd.read_csv('data/Uber_Eats_data (2).csv')

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Rename column
df.rename(columns={
    'approx_cost(for two people)': 'approx_cost_for_two'
}, inplace=True)

# -------------------------
# Clean cost column
# -------------------------
df['approx_cost_for_two'] = df['approx_cost_for_two'].astype(str).str.replace(',', '')
df['approx_cost_for_two'] = pd.to_numeric(df['approx_cost_for_two'], errors='coerce')

# -------------------------
# Clean rating column
# -------------------------
df['rate'] = df['rate'].astype(str)
df['rate'] = df['rate'].str.replace('/5', '', regex=False)
df['rate'] = df['rate'].replace(['NEW', '-', ''], None)
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

# Fill missing ratings
df['rate'].fillna(df['rate'].median(), inplace=True)

# -------------------------
# Clean other columns
# -------------------------
df['online_order'] = df['online_order'].str.strip().str.lower()
df['book_table'] = df['book_table'].str.strip().str.lower()

# Remove duplicates
df.drop_duplicates(inplace=True)

# -------------------------
# Feature Engineering
# -------------------------
def price_category(cost):
    if cost < 300:
        return 'Low'
    elif cost <= 700:
        return 'Mid'
    return 'Premium'

df['price_category'] = df['approx_cost_for_two'].apply(price_category)

# -------------------------
# Save cleaned file
# -------------------------
df.to_csv('data/cleaned_restaurants.csv', index=False)

print("✅ Cleaned file created successfully!")