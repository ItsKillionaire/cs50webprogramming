Core Python Concepts

Hello, World!

The simplest Python program prints "hello, world" to the console.
Python

print("hello, world")

To run this, save it as hello.py and execute python hello.py in the terminal. Python is an interpreted language, meaning the interpreter reads and executes the .py file line by line.

Variables and Types

Python uses variables to store values without requiring explicit type declaration. Python infers the type.

    int: Whole numbers (e.g., 28)

    float: Numbers with decimal points (e.g., 1.5)

    str: Text, enclosed in single or double quotes (e.g., "hello", 'world')

    bool: Boolean values, True or False (capitalized)

    NoneType: Represents the absence of a value, None (capitalized)

User Input

The input() function prompts the user for input, always returning a string.
Python

name = input("Name: ")
print(f"Hello, {name}")

To convert input to an integer, use int():
Python

n = int(input("Number: "))

String Manipulation

Strings can be concatenated using the + operator or formatted using f-strings (formatted strings).
Python

# Concatenation

print("hello, " + name)

# F-string

print(f"hello, {name}")

Control Flow

Conditions

Python uses if, elif (else-if), and else for conditional execution. Indentation is crucial as it defines code blocks.
Python

n = int(input("Number: "))

if n > 0:
print("n is positive")
elif n < 0:
print("n is negative")
else:
print("n is zero")

Loops

for loops iterate over sequences.
Python

# Looping through a list

for i in [0, 1, 2, 3, 4, 5]:
print(i)

# Using range() for a sequence of numbers

for i in range(6): # Generates 0 to 5
print(i)

# Looping through a string

name = "Harry"
for char in name:
print(char)

Data Structures

Python offers various sequence types and data structures:

    str (String): Immutable sequence of characters.
    Python

name = "Harry"
print(name[0]) # Output: H

list: Mutable sequence of values, defined with square brackets [].
Python

names = ["Harry", "Ron", "Hermione"]
print(names[0]) # Output: Harry
names.append("Ginny") # Adds "Ginny" to the end
names.sort() # Sorts the list alphabetically
print(names)

tuple: Immutable sequence of values, defined with parentheses (). Often used for fixed collections like coordinates.
Python

coordinate = (10.0, 20.0)

set: Unordered collection of unique values, defined with set() or curly braces {}.
Python

s = set() # Creates an empty set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) # Will not add a duplicate
s.remove(2)
print(s) # Output: {1, 3, 4} (order may vary)
print(f"The set has {len(s)} elements.")

dict (Dictionary): A collection of key-value pairs, defined with curly braces {}. Keys must be unique.
Python

    houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
    print(houses["Harry"]) # Output: Gryffindor
    houses["Hermione"] = "Gryffindor" # Adds a new entry
    print(houses["Hermione"])

Comments

Use the # symbol for single-line comments.
Python

# This is a comment

Functions and Modularity

Defining Functions

Functions are defined using the def keyword, taking arguments in parentheses and returning a value with return.
Python

def square(x):
return x \* x

for i in range(10):
print(f"The square of {i} is {square(i)}")

Modules

Code can be organized into separate .py files (modules). Functions from one module can be imported and used in another.
Suppose functions.py contains square(x):
Python

# In squares.py

# Option 1: Import a specific function

from functions import square
print(square(5))

# Option 2: Import the whole module

import functions
print(functions.square(5))

Python has many built-in modules (e.g., math, sys, csv).

Object-Oriented Programming (OOP)

Classes and Objects

Classes are blueprints for creating objects, which can store data (attributes) and perform actions (methods).
Python

class Point:
def **init**(self, x, y):
self.x = x
self.y = y

p = Point(2, 8)
print(p.x) # Output: 2
print(p.y) # Output: 8

The **init** method is a special "magic method" called automatically when a new object is created. self refers to the instance of the object.

Example: Flight Class

Python

class Flight:
def **init**(self, capacity):
self.capacity = capacity
self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
if flight.add_passenger(person):
print(f"Added {person} to flight successfully.")
else:
print(f"No available seats for {person}.")

This demonstrates how methods like add_passenger operate on the object's data (self.passengers, self.capacity).

Advanced Topics

Decorators

Decorators are a way to modify functions by wrapping them with additional behavior. They use the @ syntax.
Python

def announce(f):
def wrapper():
print("About to run the function...")
f()
print("Done with the function.")
return wrapper

@announce
def hello():
print("Hello, world!")

hello()

Output:

About to run the function...
Hello, world!
Done with the function.

Decorators are powerful for adding common functionality (e.g., logging, authentication) to multiple functions.

Lambda Expressions

Lambda expressions are small, anonymous functions defined in a single line. They are often used for sorting or filtering.
Python

people = [
{"name": "Harry", "house": "Gryffindor"},
{"name": "Cho", "house": "Ravenclaw"},
{"name": "Draco", "house": "Slytherin"}
]

# Sort by name using a lambda

people.sort(key=lambda person: person["name"])
print(people)

Output (sorted by name):

[{'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}, {'name': 'Harry', 'house': 'Gryffindor'}]

Exception Handling

Python uses try and except blocks to gracefully handle errors (exceptions) that might occur during program execution.
Python

import sys

try:
x = int(input("x: "))
y = int(input("y: "))
except ValueError:
print("Error: Invalid input.")
sys.exit(1)

try:
result = x / y
except ZeroDivisionError:
print("Error: Cannot divide by zero.")
sys.exit(1)

print(f"{x} / {y} = {result}")

This example handles ValueError (if input isn't a number) and ZeroDivisionError (if dividing by zero), preventing the program from crashing and providing user-friendly messages.
