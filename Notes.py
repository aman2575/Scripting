
### Type Hint

# def increment(num, inc=1):
#     return num + inc
# print(increment(1))

# Using Type hint
# def increment(num: int, inc: int =1 ):
#     return num + inc
# print(increment(1))
# Or
# def increment(num: int, inc: int = 1) -> int:
#     return num + inc
# print(increment(1))
# help(increment)

#  Generic Aliases
# def list_sum(l: list):
#     return sum(l)
# Using Type Hint
# from typing import List
# def list_sum(l: List[int]):
#     return sum(l)
# help(list_sum)


# def divide(a,b):
#     return a/b
# help(divide)
# Using Type hint we can reframe the above as
# from typing import Union
# def divide(a: Union[int, float], b: Union[int, float]):
#     return a/b
# help(divide)

# def anything(a):
#     print(a)
# help(anything)
# Using above the above can be framed as 
# from typing import Any
# def anything(a: Any):
#     print(a)
# help(anything)

# def add(a,b):
#     return a+b
# help(add)
# Using Hint the above can be written as, since a and b can be any variable, int or char or float, typevar helps to use same datatype for a and b
# from typing import TypeVar
# T = TypeVar('T')
# def add(a: T, b: T) -> T:
#     return a+b
# help(add)

### Type Checking in Python using mypy, to check type errors
# from typing import List
# def list_sum(l: List[int]) -> int:
#     return sum(l)
# mylist = [1,2,3,4,"a"]
# print(list_sum(mylist))
# help(list_sum)

### DataClasses in Python
# Earlier we used to write like this
# class Person:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def __repr__(self):
#         return "Person(name={}, age={}, city={})".format(self.name, self.age, self.city)
#     def __eq__(self, other):
#         return (self.name, self.age, self.city) == (other.name, other.age, other.city)
# Using Dataclasses
# from dataclasses import dataclass
# @dataclass
# class NewPerson:
#     name: str
#     age: int
#     city: str
# p1 = NewPerson('Aman',25,"Delhi")
# p2 = NewPerson('Aman',25,"Delhi")
# print(p1==p2)


### Common Packages and Modules




## Async.io
"""
Comparision Chart  (https://www.youtube.com/watch?v=Qb9s3UiMSTA)
Asyncio
    - For managing many writing tasks

    # Event Loop
    
    # Coroutine

    # Tasks

    # Gather function

    # TaskGroup

    # Futures  ( Not used usually, only with low level code)

    # Synchronization
        - Lock
    # Semaphore
        - Allows multiple coroutines to have access to the same object at the same time
    # Event

- Processes 
    - For Maximizing performance on CPU intensive tasks
- Threads
    - For Parallel task that share data with minimal CPU Use

"""



### Python Dotenv
# import os
# from dotenv import load_dotenv

# load_dotenv(override=True)  ## override=True, if want to override system wide env variable

# API_KEY = os.getenv("API_KEY")
# USERNAME = os.getenv("USERNAME")
# ADDRESS = os.getenv("ADDRESS")
# US = os.getenv("MAIL")
# # print(API_KEY)
# # print(USERNAME)
# # print(ADDRESS)
# print(US)

### Numpy

# Numpy is a general-purpose array
# import numpy as np
# print(np.arange(1,10,0.5))
#print(np.linspace(1,100,20))

# Array Reshaping
# arr = np.array([[1,2,3,4,5,6,7,8]])
# print(arr.shape)
# print(arr.reshape(2,4))
# print(arr.reshape(4,2))
# print(arr.reshape(2,2,2))
# print(arr.reshape(8,))


# Array Flattening
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.flatten(order='F'))  ##  Cloumn major ordering
# print(arr.flatten(order='C'))  ## Row major ordering
# print(arr.reshape(6))


# Array Indexing
# Positive tuple indexing
# arr = np.array([[-1,2,0,4],
#                 [4,-0.5,6,0],
#                 [2.6,0,7,8],
#                 [3,-7,4,2.0]])
#print(arr[2,1])

# Slicing: Just like list in python, Numpy arrays can be sliced. as arrays can be multidimensional, you need to specify a slice for each dimension of the array

# To get 1st two rows 
# print(arr[:2])

# To get 1st two columns
# print(arr[:,:2])

# TO get 1st two rows and 1st 3 coloumns
# print(arr[:2,:3])

# Integer array indexding: In this method, list are passed for indexing for each dimension, One to one mapping of corresponding elements is done to construct a new arbitrary array
# print(arr[[0,1,2,3],[0,1,2,3]])

# Boolean array Indexing: This methods is used when we want to pick elements from array which satisfy some condition
# print(arr>0)
# print(arr[arr>0])


## Array Operation
# Elementwise operation: We can use overloaded arithmetic operation to do element-wise operation on array to create a new array. In case pf +=,-=,*= operators, the existing array is modified 
# arr = np.array([[1,2,3],
#                 [4,5,6]])
# print(arr)
# print(arr +1)
# print(arr **2)
# arr +=1
# print(arr)

# Unary operators: Many unary operation are provided as a method of ndarray class. This includes sum,min,max, etc. These functions can also be applied row-wise or column-wise by setting an axis parameter
# print(arr.sum())
# print(arr.sum(axis=0))
# print(arr.sum(axis=1))
# print(arr.min(axis=0))
# print(arr.max(axis=1))

# Binary operations: THe operations apply on array elementwise and a new array is created. You can use all basic arithemetic operators like +,-,/,*,etc. In case of +=,-=,*= operators, the exsisting array is modified.
# a = np.array([[1,2],
#               [3,4]])
# b = np.array([[5,6],
#               [7,8]])
# print(a+b)

# Universal functions(ufunc): Numpy provides familiar mathematical function such as sin,cos,exp,etc. These function also operate elementwise on an array, producing an array as output
# NOTE: All the operation we did above using overloaded operation cab be done using ufunc like np.add, np.subtract, np.multiply, np.divide, np.sum, etc

# print(arr)

# print(np.sin(arr))
# print(np.exp(arr))

## Array Sorting
# Ther is a simple np.sort method for sorting NumPy arrays
# arr = np.array([[1,4,2],
#                 [3,4,6],
#                 [0,-1,5]])
# print(arr)
# print(np.sort(arr, axis=1)) # Row wise sorting
# print(np.sort(arr, axis=0)) # column wise sorting

# Sorting all my arrays in 1D format
# print(np.sort(arr, axis=None))

## Array Stacking and Splitting
# Stacking
# Serveral array can be stacked together along different axes
"""
- np.vstack: To stack arrays along vertical axis
- np.hstack: To stack arrays along horizontal axis
- np.column_stack: To stack 1-D arrays as columns into 2-D arrays
- np.row_stack: To stack 1-D arrays as rows into 2-D arrays
- np.concatenate: To stack arrays along specified axis(axis is passed as argument)

"""
# a = np.array([[1,2],
#               [3,4]])
# b = np.array([[5,6],
#               [7,8]])
# print(a)
# print(b)
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))
# Let's say you have a single column
# c = np.array([0,0])
# print(c)
# print(np.column_stack((a,c)))
# print(np.row_stack((a,c)))
# For multiple array more than 2 we use concatenation 
# print(np.concatenate((a,b), axis=1))
# print(np.concatenate((a,b), axis=0))

# Splitting
# for splitting, we have these functions:
"""
- np.hsplit: Split array alon horizontal axis
- np.vsplit: Split array alon vertical axis
- np.array_split: Split array along specified axis.
"""
# a = np.array([[1,3,5,7,9,11],
#               [2,4,6,8,10,12]])

# print(np.hsplit(a,2))
# print(np.vsplit(a,2))
# When we have more the 2D array we use array_split
# print(np.array_split(a,2,axis=1))

## Array Broadcasting
# The term broadcasting describes how numpy treats array with different shapes during arithmetic operation.

## Working with Datetime

## Linear Algebra

## Saving & Loading Arrays

###Pandas


### Polars

### Generator Expression
# https://www.pythontutorial.net/advanced-python/python-generator-expressions/

### Context Manager
# https://www.pythontutorial.net/advanced-python/python-context-managers/

### PAradigms
## Procedural Programming
# docuses on writing procedures or functions that operate on data. This paradigm emphasizes a sequence of steps to be followed
# def greet(name):
#     print("Hello, " + name + "!")

# name = "Tutorialspoint"
# greet(name)
##Object-Oriented Programming (OOP)
# OOP organizes code into objectsm which are instances of classes, This paradigm promotes encapsulation, inheritance, and polymorphism
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         raise NotImplementedError("Subclass must implement this method.")

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# dog = Dog("Buddy")
# print(dog.name)
# print(dog.speak())

## Imperative Programming
# It involves writing code that specifies detailed steps to achieve a goal. 
# focuses on how to perform tasks through statements that change the program state.
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print("Sum:", total)

## Function Programming
# treats computation as the evaluation of mathematical functions. It emphasize immutability and the ise of pure functions.
# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x ** 2, numbers))
# print("The square of the numbers in the list:", squares)

# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print("The even numbers from the given list:", even_numbers)

## Event-Driven Programming
# is centered around events and their handlers, often used in GUI applications and asynchronous programming
# from tkinter import Tk, Button

# def button_click():
#     print("Button clicked!")

# root = Tk()
# button = Button(root, text="Click me", command=button_click)
# button.pack()
# root.mainloop()
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
