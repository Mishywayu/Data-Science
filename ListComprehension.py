# List comprehension is used to iterate through lists without explicitly writing loops, 
# which is especially useful for filtering data according to a specific condition.

# Let's take a look at a list that shows property prices in Mexican pesos.
price_mexican_pesos = [
    35000000.0,
    2000000.0,
    2700000.0,
    6347000.0,
    6994543.16,
    6617835.61,
    670000.0,
]
# But maybe we're interested in comparing these prices to property values in Colombia. 
# To do that, we'll need to figure out how to express the data on our list in Colombian pesos. 
# We can use a for loop to make the conversion based on an exchange rate of 1 Mexican peso to 190 
# Colombian pesos. The code looks like this:
price_colombian_pesos = []
for price in price_mexican_pesos:
    price_colombian_pesos.append(price * 190)
print(price_colombian_pesos)
# But what if we could do the same thing, but using fewer lines? 
# That's what list comprehension is for. 
# The code looks like this:
price_colombian_pesos = [price * 190 for price in price_mexican_pesos]
print(f"This is the output for using list comprehension. {price_colombian_pesos}")