#Variables


# Abstractions 
# car 

# 1. has/have 
#    properties/attributes 

#     1. tires  -> list 
#               has/have 
#                    shape/size
#      2. brakes 
#      3. wheels



# 2. does/ functions   
#   takes from point A to point B                 




# Numeric types
num_int = 5
num_float = 5.5
num_complex = 2 + 3j

# Sequence types
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_range = range(1-5)

# Text type
my_str = "Hello, World!"

# Set types
my_set = {1, 2, 3}
my_frozenset = frozenset([1, 2, 3])

# Mapping type
my_dict = {'name': 'Alice', 'age': 25}

# Boolean type
is_valid = True

# Binary types
my_bytes = b'hello'
my_bytearray = bytearray(b'hello')
my_memoryview = memoryview(my_bytes)

# None type
no_value = None




# Here are code examples demonstrating each of the  built-in functions listed:

# 1. Type and Conversion Functions


# type
print()
print(type(5))               # Output: <class 'int'>

# int, float, str
print(int("10"))             # Output: 10
print(float("5.5"))          # Output: 5.5
print(str(123))              # Output: "123"

# bool
print(bool(0))               # Output: False
print(bool(1))               # Output: True

# list, tuple, set
print(list("abc"))           # Output: ['a', 'b', 'c']
print(tuple("abc"))          # Output: ('a', 'b', 'c')
print(set("abc"))            # Output: {'a', 'b', 'c'}


2. Mathematical Functions


# abs
print(abs(-5))               # Output: 5

# round
print(round(5.678, 2))       # Output: 5.68

# min, max
print(min([1, 2, 3]))        # Output: 1
print(max([1, 2, 3]))        # Output: 3

# sum
print(sum([1, 2, 3]))        # Output: 6

# pow
print(pow(2, 3))             # Output: 8 (2^3)
3. String Functions


# len
print(len("hello"))          # Output: 5

# str
print(str(123))              # Output: "123"

# format
print("Hello, {}".format("world"))  # Output: Hello, world
4. Input and Output Functions


# print
print("Hello, World!")       # Output: Hello, World!

# input (uncomment to use in an interactive environment)
# name = input("Enter your name: ")
# print("Hello, " + name)

# open (reads a file and prints each line)
with open("sample.txt", "w") as f:
    f.write("This is a sample file.")
    
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())   # Output: This is a sample file.



5. Data Structure Functions


# sorted
print(sorted([3, 1, 2]))     # Output: [1, 2, 3]

# reversed
print(list(reversed([1, 2, 3])))  # Output: [3, 2, 1]

# enumerate
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)       # Output: 0 a, 1 b, 2 c

# zip
for item in zip([1, 2], ['a', 'b']):
    print(item)               # Output: (1, 'a'), (2, 'b')
6. Functional Programming Tools


# map
print(list(map(str.upper, ['a', 'b'])))  # Output: ['A', 'B']

# filter
print(list(filter(lambda x: x > 0, [-1, 0, 1])))  # Output: [1]

# reduce (requires functools)
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3]))  # Output: 6

# lambda
add_one = lambda x: x + 1
print(add_one(5))            # Output: 6


7. Utility Functions


# id
x = 5
print(id(x))                 # Output: memory address of `x`

# any
print(any([False, True, False]))  # Output: True

# all
print(all([True, True, False]))   # Output: False

# isinstance
print(isinstance(5, int))     # Output: True

# dir
print(dir([]))                # Output: List of attributes and methods for a list object
8. Exception Handling


# raise
try:
    raise ValueError("Invalid value")
except ValueError as e:
    print(e)                  # Output: Invalid value

# assert
assert 5 > 3, "5 is not greater than 3"   # Does nothing, assertion is True
# assert 5 < 3, "5 is not greater than 3"   # Raises AssertionError: 5 is not greater than 3


9. Object-Oriented Functions


class MyClass:
    def __init__(self, value):
        self._value = value

    # property
    @property
    def value(self):
        return self._value

    # classmethod
    @classmethod
    def create_with_value(cls, value):
        return cls(value)

    # staticmethod
    @staticmethod
    def is_positive(number):
        return number > 0

obj = MyClass(10)
print(obj.value)                   # Output: 10
print(MyClass.is_positive(5))      # Output: True
print(MyClass.create_with_value(20).value)  # Output: 20


1. Lists


my_list = [1, 2, 3, "hello"]
my_list.append("world")
print(my_list)  # Output: [1, 2, 3, 'hello', 'world']
2. Tuples


my_tuple = (1, 2, 3, "hello")
print(my_tuple[0])  # Output: 1
# Tuples are immutable, so you cannot change or add elements.
3. Dictionaries


my_dict = {"name": "Alice", "age": 25}
my_dict["age"] = 26  # Update value
print(my_dict)  # Output: {'name': 'Alice', 'age': 26}
4. Sets


my_set = {1, 2, 3, 3}  # Duplicate '3' is ignored
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
5. Frozensets


my_frozenset = frozenset([1, 2, 3])
# Frozensets are immutable, so you cannot add or remove elements.
print(my_frozenset)  # Output: frozenset({1, 2, 3})
6. Strings


my_str = "Hello, World!"
print(my_str.upper())  # Output: "HELLO, WORLD!"
print(my_str[0])  # Output: "H" (Strings are indexed like lists)
7. Arrays


from array import array
my_array = array("i", [1, 2, 3])  # "i" means signed integer type
my_array.append(4)
print(my_array)  # Output: array('i', [1, 2, 3, 4])
8. Deque (Double-Ended Queue)


from collections import deque
my_deque = deque([1, 2, 3])
my_deque.appendleft(0)  # Add to the left end
my_deque.append(4)      # Add to the right end
print(my_deque)  # Output: deque([0, 1, 2, 3, 4])
9. NamedTuples


from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)  # Output: 10 20
10. Defaultdict


from collections import defaultdict
my_defaultdict = defaultdict(int)  # Default value of int() is 0
my_defaultdict["missing"] += 1
print(my_defaultdict)  # Output: defaultdict(<class 'int'>, {'missing': 1})
11. Counter


from collections import Counter
my_counter = Counter(["a", "b", "a", "c", "b", "b"])
print(my_counter)  # Output: Counter({'b': 3, 'a': 2, 'c': 1})
12. OrderedDict


from collections import OrderedDict
my_ordered_dict = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
print(my_ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
13. Heap Queue (Priority Queue)


import heapq
my_heap = [3, 1, 4, 1, 5]
heapq.heapify(my_heap)  # Transform list into a heap
print(my_heap)  # Output: [1, 1, 4, 3, 5]
heapq.heappush(my_heap, 0)  # Add a new element
print(my_heap)  # Output: [0, 1, 4, 3, 5, 1]
smallest = heapq.heappop(my_heap)  # Remove the smallest element
print(smallest)  # Output: 0
14. Linked List (Custom Implementation)
 doesn’t have a built-in linked list, but we can create one using classes.



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

# Usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
15. Binary Tree and Graphs (Custom Implementation)
Similarly, binary trees and graphs aren’t built-in but can be implemented with classes.

Binary Tree Example


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

Graph Example (Adjacency List Representation)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

# Usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
print(g.graph)  # Output: {1: [2, 3]}



1. Conditionals
if Statement
Executes code only if a specified condition is True.



x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5
if...else Statement
Provides an alternative action if the condition is False.



x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")  # Output: x is not greater than 5
if...elif...else Statement
Allows multiple conditions to be checked in sequence.



x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")  # Output
else:
    print("x is 5 or less")
Ternary Conditional Operator
A shorthand for if...else in a single line.



x = 5
message = "x is even" if x % 2 == 0 else "x is odd"
print(message)  # Output: x is odd
2. Loops
for Loop
Used to iterate over a sequence (such as a list, tuple, dictionary, set, or string).



# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
for Loop with range()
The range() function generates a sequence of numbers. It's commonly used with for loops.



for i in range(5):  # Generates numbers from 0 to 4
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
for Loop with enumerate()
enumerate() provides both the index and value of each item in the loop.



fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry
for Loop with break and continue
break stops the loop, while continue skips the current iteration.



for i in range(5):
    if i == 3:
        break  # Exits loop when i is 3
    print(i)
# Output: 0 1 2

for i in range(5):
    if i == 3:
        continue  # Skips printing when i is 3
    print(i)
# Output: 0 1 2 4
while Loop
Executes as long as a condition is True.



i = 0
while i < 5:
    print(i)
    i += 1
# Output:
# 0
# 1
# 2
# 3
# 4
while Loop with break and continue
Just like with for loops, break and continue can control flow within a while loop.



i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
# Output: 0 1 2

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5
Nested Loops
Loops inside other loops. Each iteration of the outer loop triggers the inner loop to complete all its iterations.



for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
# Output:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1
3. Loop Control Statements
pass Statement
Used as a placeholder in a loop or conditional where code is syntactically required but nothing needs to be executed.



for i in range(5):
    if i == 3:
        pass  # No operation here
    print(i)
# Output: 0 1 2 3 4
