"""SELECT business_id, business_name, rating 
FROM business 
ORDER BY rating DESC
LIMIT 5"""

"""SELECT business_id, business_name, rating 
FROM business 
ORDER BY rating
LIMIT 5"""

"""SELECT AVG(rating) as averageOne
FROM business 
WHERE price = '$' """

"""SELECT COUNT(rating) as aboveFourHalf
FROM business 
WHERE rating > 4.5"""


"""SELECT COUNT(rating) as underThree
FROM business 
WHERE rating < 3"""
