# Tasks to practice with lambda functions in Python:


# Task 1: Extract Words Starting with a Specific Letter
# Given a list of words, use a lambda function to filter out 
# words that start with the letter 'a'.
words = ["apple", "banana", "cherry", "avocado", "grape"]

def wordA(words):
    for word in words:
        if word[0] == 'a':
            print (word)
print(f"Above output for normal function task 1 {wordA(words)}")

#LAMBDA
wordLambda = lambda words: [word for word in words if word[0] == 'a']
print(f"Above output for normal function task 1 {wordLambda(words)}")


# Task 2: Create a List of Squares
# Create a list of squares for numbers from 1 to 10 using map() and a lambda function.
numbers = range(1,10)

def listSquares():
    return list(map(lambda x: x**2, numbers))
print(f"output for normal function task 2 {list(listSquares())}")

# LAMBDA
squares = map(lambda x: x**2, numbers)
print(f"output for lambda fuction task 2 {list(squares)}")



# Task 3: Sort Strings by Length
# Given a list of strings, use a lambda function to sort the strings based on their
# lengths in descending order.
strings = ["short", "longer", "tiny", "a very long string"]

def lengthStr(strings):
    sorted_strings = sorted(strings, key=len, reverse=True)
    print(sorted_strings)
print (f"Output for Task 3, normal function: {lengthStr(strings)}")

# LAMBDA
length = lambda strings: sorted(strings, key=len, reverse=True)
print(f"Output for task 3, Lambda function: {length(strings)}")