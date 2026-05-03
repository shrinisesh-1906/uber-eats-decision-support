TOP_LOCATIONS = """
SELECT location, AVG(rating) AS avg_rating
FROM restaurants
GROUP BY location
ORDER BY avg_rating DESC
LIMIT 10
"""

OVER_SATURATED = """
SELECT location, COUNT(*) AS total_restaurants
FROM restaurants
GROUP BY location
ORDER BY total_restaurants DESC
LIMIT 10
"""

ONLINE_ORDER_IMPACT = """
SELECT online_order, AVG(rating) AS avg_rating
FROM restaurants
GROUP BY online_order
"""

PRICING_ANALYSIS = """
SELECT price_category, AVG(rating) AS avg_rating
FROM restaurants
GROUP BY price_category
"""

TOP_CUISINES = """
SELECT cuisines, COUNT(*) AS count
FROM restaurants
GROUP BY cuisines
ORDER BY count DESC
LIMIT 10
"""
AVG_ORDER_VALUE = """
SELECT AVG(order_value) AS avg_order_value
FROM orders
"""

ORDER_VOLUME = """
SELECT restaurant_name, COUNT(*) AS total_orders
FROM orders
GROUP BY restaurant_name
ORDER BY total_orders DESC
LIMIT 10
"""

PAYMENT_METHOD = """
SELECT payment_method, COUNT(*) AS total
FROM orders
GROUP BY payment_method
"""

DISCOUNT_IMPACT = """
SELECT discount_used, AVG(order_value) AS avg_value
FROM orders
GROUP BY discount_used
"""

BEST_RESTAURANTS = """
SELECT r.name, r.location,
       AVG(o.order_value) AS avg_order_value,
       COUNT(o.order_id) AS total_orders
FROM restaurants r
JOIN orders o
ON r.name = o.restaurant_name
GROUP BY r.name, r.location
ORDER BY avg_order_value DESC
LIMIT 10
"""