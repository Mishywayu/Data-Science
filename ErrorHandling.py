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