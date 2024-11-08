# ITERATORS and ITERABLES
# ITERATOR - is an object that implements the iterator protocol, 
#             which consists of the methods __iter__() and __next__().
                # You can create an iterator from an iterable by using the iter() function, 
                # which returns an iterator object. The next() function can then be used to 
                # retrieve elements from the iterator one at a time.
# ITERABLE - is any object that can return its members one at a time, 
#            allowing it to be iterated over in a loop. Examples of iterables include 
#            lists, tuples, dictionaries, sets, and strings.


# Example of an Iterable
list = ['A', 'B', 'C', 'D', 'E', 'F']

for char in list:
    print (f"This is the output of the Iterable example, which prints {char}")

# Example of an Iterator
listA = ['A', 'B', 'C', 'D', 'E']
my_iterator = iter(listA)
print(f"This is output for Iterator example. The output is {next(my_iterator)}")
print(f"This is output for Iterator example. The output is {next(my_iterator)}")
print(f"This is output for Iterator example. The output is {next(my_iterator)}")