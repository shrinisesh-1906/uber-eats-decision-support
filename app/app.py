import streamlit as st
import pandas as pd
import sqlite3
import queries

# DB Connection
conn = sqlite3.connect('database/database.db')

st.title("Uber Eats Decision Support System")

# -----------------------------
#  SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

locations = pd.read_sql("SELECT DISTINCT location FROM restaurants", conn)
selected_location = st.sidebar.selectbox("Select Location", ["All"] + locations['location'].tolist())

price = pd.read_sql("SELECT DISTINCT price_category FROM restaurants", conn)
selected_price = st.sidebar.selectbox("Select Price Category", ["All"] + price['price_category'].tolist())

online = st.sidebar.selectbox("Online Order", ["All", "yes", "no"])

# -----------------------------
#  DYNAMIC QUERY
# -----------------------------
query = "SELECT * FROM restaurants WHERE 1=1"

if selected_location != "All":
    query += f" AND location = '{selected_location}'"

if selected_price != "All":
    query += f" AND price_category = '{selected_price}'"

if online != "All":
    query += f" AND online_order = '{online}'"

df_filtered = pd.read_sql(query, conn)

st.subheader(" Filtered Results")
st.dataframe(df_filtered)

# -----------------------------
#  BUSINESS QUESTIONS
# -----------------------------
st.subheader("Business Questions")

option = st.selectbox("Choose Question", [
    "Top Locations by Rating",
    "Over-saturated Locations",
    "Online Order Impact",
    "Table Booking Impact",
    "Price vs Rating",
    "Top Cuisines",
    "Top Rated Cuisines",
    "Niche Cuisines",
    "Premium Locations",
    "Best Restaurants"
])

if option == "Top Locations by Rating":
    df_q = pd.read_sql(queries.TOP_LOCATIONS, conn)

elif option == "Over-saturated Locations":
    df_q = pd.read_sql(queries.OVER_SATURATED, conn)

elif option == "Online Order Impact":
    df_q = pd.read_sql(queries.ONLINE_ORDER_IMPACT, conn)

elif option == "Table Booking Impact":
    df_q = pd.read_sql(queries.TABLE_BOOKING_IMPACT, conn)

elif option == "Price vs Rating":
    df_q = pd.read_sql(queries.PRICE_ANALYSIS, conn)

elif option == "Top Cuisines":
    df_q = pd.read_sql(queries.TOP_CUISINES, conn)

elif option == "Top Rated Cuisines":
    df_q = pd.read_sql(queries.TOP_RATED_CUISINES, conn)

elif option == "Niche Cuisines":
    df_q = pd.read_sql(queries.NICHE_CUISINES, conn)

elif option == "Premium Locations":
    df_q = pd.read_sql(queries.PREMIUM_LOCATIONS, conn)

elif option == "Best Restaurants":
    df_q = pd.read_sql(queries.BEST_RESTAURANTS, conn)

# Display
st.subheader("Result")
st.dataframe(df_q)
st.write("Total Rows:", len(df_q))

