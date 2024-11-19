# Error handling in Python is the process of catching, handling, and recovering 
# from exceptions or errors that occur during the execution of code. 
# It helps prevent crashes, provides useful feedback to users, and ensures 
# code runs smoothly even under unexpected conditions.

# A brief overview of error handling and some common examples:
# Basic Syntax of Error Handling with try, except, else and finally
#     *try: The lock of code where you suspect an error might occur.
#     *except: The block that handles the error if it occurs.
#     *else: (Optional) The block that runs if no error occurs.
#     *finally: (Optional) The block that runs whether or not an error occurs.

# EXAMPLE CODE
try:
    # Code that might raise an exception
    c = 10 + 20
except AdditionError as e: # type: ignore
    # Hanlde the specific error
    print(f"Error occured: {e}")
else:
    # Code that runs if no error occurs
    print(f"Addition was successfull")
finally:
    # Code that runs whether or not an error occurs(ALWAYS RUNS)
    print(f"This is the end of the try-except block")



 # PRACTICE
def find_max_price_per_area(price_per_meter2):
    """Find the most expensive price per unit areas given a list

    Parameters
    ----------
    price_per_meter : list of int
        List with price per unit area of each property

    Returns
    -------
    the price of the most expensive property per unit area
    """
    try:
        max_price = max(price_usd_per_m2)
    except:
        print(f"Couldn't find max price, an error occured")
    else:
        print(f"Max price was found. It is {max_price}")
    
price_usd_per_m2 = [9799, 880.53, 176] #successfull
# price_usd_per_m2 = ["190", 368.53, 1764] #prints error
find_max_price_per_area(price_usd_per_m2)
