# When we code in Python, we want to create readable programs. 
# One of the easiest ways to make a program readable is by not 
# repeating sections of code that do the same thing. We do that 
# by using functions. For example, you might have surface area 
# of a property in square meters, but you want to see it in square feet. 
# Keeping in mind that one square meter = 10.76391 square feet, 
# you can write a function that starts with the area in square meters, 
# and gives as output the area in square feet. The code looks like this:

def m2toft2(area_meter2):
    area_feet2 = 10.76391 * area_meter2
    return area_feet2

print(m2toft2(4))


# A function by itself can be difficult to understand, 
# so let's add some comments describing what the function does.
def m2toft2(area_meter2):
    """
    This function takes in as input the area in meters squared
    and returns as an output the area in square feet

    input: area_meter2, the area in square meters
    output: area_feet2, the area in square feet
    """
    area_feet2 = 10.76391 * area_meter2
    return area_feet2

help(m2toft2)


# PRACTICE
# Write a function that returns the greatest per unit area property price
# for a list of property prices per unit area and then use your function for the list
# price_usd_per_m2

price_usd_per_m2 = [97996.85, 36880.53, 176499.72]

def find_max_price_per_area(price_usd_per_m2):
    max_price = max(price_usd_per_m2)
    return max_price
print(f"The max price is {find_max_price_per_area(price_usd_per_m2)}")


# PRACTICE 2
# The previous example does not extend the max function that is in Python.
# Keeping in mind that list comprehensions can be used to iterate through lists, 
# use list comprehension or loops to write a function which, given a list of property 
# areas and a corresponding list of property prices per unit area, returns the total 
# price of the most expensive property.

def find_max_price(area_meter2, price_per_meter2):
    """
    Given two lists, the first with areas of properties
    and the second with price per unit area, this function
    returns the most expensive property using list comprehension

    input: area_meter2, list with the total area of each property
    input: price_per_meter2, list with price per unit area of each property
    output: the price of the most expensive property
    """
    total_prices = [area * price for area, price in zip(area_meter2, price_per_meter2)]
    return max(total_prices) if total_prices else None


find_max_price(surface_total_in_m2, price_usd_per_m2)