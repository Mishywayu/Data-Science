# Tasks to practice with lambda functions in Python:


# Task 1: Extract Words Starting with a Specific Letter
# Given a list of words, use a lambda function to filter out 
# words that start with the letter 'a'.

#Normal Function
words = ["apple", "banana", "cherry", "avocado", "grape"]
def wordA(words):
    for word in words:
        if word[0] == 'a':
            print (word)
print(f"Above output for normal function task 1 {wordA(words)}")


#Lambda Function
wordLambda = lambda words: [word for word in words if word[0] == 'a']
print(f"Above output for normal function task 1 {wordLambda(words)}")


# Task 2: Create a List of Squares
# Create a list of squares for numbers from 1 to 10 using map() and a lambda function.
numbers = range(1,10)
def listSquares():
    return list(map(lambda x: x**2, numbers))
print(f"output for normal function task 2 {list(listSquares())}")

squares = map(lambda x: x**2, numbers)
print(f"output for lambda fuction task 2 {list(squares)}")