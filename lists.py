# Working with Lists
# Python comes with several data structures that we can use to organize tabular data. 
# Lets start by putting a single observation in a LIST.

# Given a books dataset.

books = [
    {
        "title": "To Kill a Mockingbird", 
        "author": "Harper Lee", 
        "year": 1960
    },
    {
        "title": "1984", 
        "author": "George Orwell", 
        "year": 1949
    },
    {
        "title": "Pride and Prejudice", 
        "author": "Jane Austen", 
        "year": 1813
    },
    {
        "title": "The Great Gatsby", 
        "author": "F. Scott Fitzgerald", 
        "year": 1925
    }
]

# INDEXING
# Accessing a specific element in the list using its index:
print(books[0])  # Output: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
print(books[1]["author"])  # Output: George Orwell

# Negative indexing: Accessing elements from the end of the list:
print(books[-1])  # Output: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
print(books[-2]["title"])  # Output: Pride and Prejudice



# SLICING:
# Extracting a subset of elements from the list:
print(books[1:3])  
# Output: [
# {"title": "1984", "author": "George Orwell", "year": 1949}, 
# {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813}
# ]
print(books[1:]) 
# Output: [
# {"title": "1984", "author": "George Orwell", "year": 1949}, 
# {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813}, 
# {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
# ]



# APPEND:
# Adding a new element to the end of the list:
books.append({"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951})
print(books)  # Output: The updated list with the new book



# INSERT:
# Adding a new element at a specific position in the list:
books.insert(2, {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1865})
print(books)  # Output: The updated list with the new book at index 2



# REMOVE:
# Deleting an element from the list:
books.remove({"title": "1984", "author": "George Orwell", "year": 1949})
print(books)  # Output: The updated list without the removed book



# POP:
# Removing and returning an element from the list:
removed_book = books.pop(1)
print(removed_book)  # Output: {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813}
print(books)  # Output: The updated list without the removed book



# SORT:
# Arranging the elements in the list in a specific order:
books.sort(key=lambda x: x["year"])
print(books)  # Output: The sorted list by year



# REVERSE:
# Reversing the order of the elements in the list:
books.reverse()
print(books)  # Output: The reversed list



# LENGTH:
# Getting the number of elements in the list:
print(len(books))  # Output: 4



# ITERATION:
# Iterating over the elements in the list:
for book in books:
    print(book["title"])
# Output:
# To Kill a Mockingbird
# 1984
# Pride and Prejudice
# The Great Gatsby



# List Comprehensions:
# Creating a new list from an existing list:
titles = [book["title"] for book in books]
print(titles)  # Output: ["To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby"]



# Filtering:
# Creating a new list with filtered elements:
classic_books = [book for book in books if book["year"] < 1950]
print(classic_books)  # Output: [{"title": "To Kill a Mockingbird", "author": "Harper Lee",