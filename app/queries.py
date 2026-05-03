# 1. Top Locations by Rating
TOP_LOCATIONS = """
SELECT location, ROUND(AVG(rating),2) AS avg_rating, COUNT(*) as total_restaurants
FROM restaurants
GROUP BY location
ORDER BY avg_rating DESC
LIMIT 10;
"""

# 2. Over-saturated Locations
OVER_SATURATED = """
SELECT location, COUNT(*) as total_restaurants
FROM restaurants
GROUP BY location
ORDER BY total_restaurants DESC
LIMIT 10;
"""

# 3. Online Order Impact
ONLINE_ORDER_IMPACT = """
SELECT online_order, ROUND(AVG(rating),2) as avg_rating
FROM restaurants
GROUP BY online_order;
"""

# 4. Table Booking Impact
TABLE_BOOKING_IMPACT = """
SELECT book_table, ROUND(AVG(rating),2) as avg_rating
FROM restaurants
GROUP BY book_table;
"""

# 5. Price vs Rating
PRICE_ANALYSIS = """
SELECT price_category, ROUND(AVG(rating),2) as avg_rating
FROM restaurants
GROUP BY price_category
ORDER BY avg_rating DESC;
"""

# 6. Most Common Cuisines
TOP_CUISINES = """
SELECT cuisines, COUNT(*) as count
FROM restaurants
GROUP BY cuisines
ORDER BY count DESC
LIMIT 10;
"""

# 7. Highest Rated Cuisines
TOP_RATED_CUISINES = """
SELECT cuisines, ROUND(AVG(rating),2) as avg_rating
FROM restaurants
GROUP BY cuisines
HAVING COUNT(*) > 10
ORDER BY avg_rating DESC
LIMIT 10;
"""

# 8. Niche Cuisines (low count, high rating)
NICHE_CUISINES = """
SELECT cuisines, COUNT(*) as total, ROUND(AVG(rating),2) as avg_rating
FROM restaurants
GROUP BY cuisines
HAVING total < 20
ORDER BY avg_rating DESC
LIMIT 10;
"""

# 9. Premium Locations (high cost + rating)
PREMIUM_LOCATIONS = """
SELECT location, ROUND(AVG(rating),2) as avg_rating
FROM restaurants
WHERE price_category = 'Premium'
GROUP BY location
ORDER BY avg_rating DESC
LIMIT 10;
"""

# 10. Best Restaurants per Price Segment
BEST_RESTAURANTS = """
SELECT name, price_category, rating
FROM restaurants
WHERE rating >= 4.5
ORDER BY rating DESC
LIMIT 20;
"""