# Lambda functions in Python are small, anonymous functions defined using the lambda keyword. 
# They are typically used for short, simple functions that are not reused elsewhere. 

# The basic syntax is:
# lambda arguments: expression

# Here's code for a function which adds 10 to a number.
add_ten = lambda c: c + 10
print(add_ten)

# This in the normal function will be:
def add_ten(c):
    return c + 10
print(f"Output for Normal Function add_ten: {add_ten(20)}")

# Now that we've defined our function, let's try it out.
# If we wanted the function to add 10 to 20, the code would look like this:
print(f"Output for Lambda Function add_ten: {add_ten(20)}") #prints out 30


# ANOTHER LAMBDA FUNCTION EXAMPLE
add = lambda x,y: x+y
print(f"Output for Lambda Function2 for add: {add(10,20)}")

# In normal function
def add(x,y):
    return x+y
print(f"Output for Normal function2 for add: {add(10,20)}")