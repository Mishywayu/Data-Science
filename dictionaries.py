# Books Dataset
books = {
    "To Kill a Mockingbird": {"author": "Harper Lee", "year": 1960},
    "1984": {"author": "George Orwell", "year": 1949},
    "Pride and Prejudice": {"author": "Jane Austen", "year": 1813},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925}
}


# Accessing Values:
# Accessing a value in the dictionary using its key:
print(books["To Kill a Mockingbird"])  # Output: {"author": "Harper Lee", "year": 1960}
print(books["1984"]["author"])  # Output: George Orwell



# Updating Values:
# Updating a value in the dictionary:
books["To Kill a Mockingbird"]["year"] = 1961
print(books["To Kill a Mockingbird"])  # Output: {"author": "Harper Lee", "year": 1961}



# Adding New Key-Value Pairs:
# Adding a new key-value pair to the dictionary:
books["War and Peace"] = {"author": "Leo Tolstoy", "year": 1865}
print(books)  # Output: The updated dictionary with the new book



# Removing Key-Value Pairs:
# Removing a key-value pair from the dictionary:
del books["1984"]
print(books)  # Output: The updated dictionary without the removed book



# Checking for Keys:
# Checking if a key exists in the dictionary:
print("Pride and Prejudice" in books)  # Output: True
print("The Catcher in the Rye" in books)  # Output: False



# Getting All Keys:
# Getting all the keys in the dictionary:
print(books.keys())  
# Output: dict_keys(['To Kill a Mockingbird', 'Pride and Prejudice', 'The Great Gatsby', 'War and Peace'])



# Getting All Values:
# Getting all the values in the dictionary:
print(books.values())  
# Output: 
# dict_values([
# {'author': 'Harper Lee', 'year': 1961},
# {'author': 'Jane Austen', 'year': 1813},
# {'author': 'F. Scott Fitzgerald', 'year': 1925},
# {'author': 'Leo Tolstoy', 'year': 1865}
# ])



# Getting All Items:
# Getting all the key-value pairs in the dictionary:
print(books.items())  
# Output: 
# dict_items([
# ('To Kill a Mockingbird', {'author': 'Harper Lee', 'year': 1961}), 
# ('Pride and Prejudice', {'author': 'Jane Austen', 'year': 1813}), 
# ('The Great Gatsby', {'author': 'F. Scott Fitzgerald', 'year': 1925}), 
# ('War and Peace', {'author': 'Leo Tolstoy', 'year': 1865})
# ])



# Iteration:
# Iterating over the key-value pairs in the dictionary:
for title, book in books.items():
    print(f"{title} by {book['author']} ({book['year']})")
# Output:
# To Kill a Mockingbird by Harper Lee (1961)
# Pride and Prejudice by Jane Austen (1813)
# The Great Gatsby by F. Scott Fitzgerald (1925)
# War and Peace by Leo Tolstoy (1865)



# Dictionary Comprehensions:
# Creating a new dictionary from an existing dictionary:
classic_books = {title: book for title, book in books.items() if book["year"] < 1950}
print(classic_books)  # Output: The new dictionary with classic books