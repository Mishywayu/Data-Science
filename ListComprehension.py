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


# PRACTICE
# Explore the list records in the list, and find all entries located in Tlalpan
records = [
    'sell,house,|México|Distrito Federal|La Magdalena Contreras|San Jerónimo Lídice|,"19.317653,-99.236291",3350000.0,MXN,3319694.98,176499.72,,350.0,,9571.42857142857',
    'sell,house,|México|Distrito Federal|Coyoacán|,"19.303906,-99.107812",7200000.0,MXN,7134866.79,379342.68,,250.0,,28800.0',
    'sell,house,|México|Distrito Federal|Venustiano Carranza|,"19.436436,-99.117256",1362000.0,MXN,1349678.96,71758.99,,98.0,,13897.959183673467',
    'sell,house,|México|Distrito Federal|Tlalpan|Granjas Coapa|,"19.300456,-99.115741",3900000.0,MXN,3864719.42,205477.28,,153.0,,25490.19607843137',
    'sell,house,|México|Distrito Federal|Coyoacán|Villa Coyoacán|,"19.348694,-99.16291",1150000.0,USD,21629775.0,1150000.0,,555.0,,2072.072072072072',
    'sell,house,|México|Distrito Federal|Tlalpan|,"19.300963,-99.144237",7500000.0,MXN,7432152.81,395148.62,,385.0,,19480.51948051948',
    'sell,house,|México|Distrito Federal|Coyoacán|Paseos de Taxqueña|,"19.343979,-99.124863",6310000.0,MXN,6252917.98,332451.71,,183.0,,34480.87431693989'
]

# Filter records to find entries that contain Tlalpan
for record in records:
    if "Tlalpan" in record:
        print(f"output without list comprehension for Tlalpan {record}")

# using list comprehension
records_tlalpan = [record for record in records if 'Tlalpan' in record]
print(f"output for Tlalpan using list comphrension{records_tlalpan}")