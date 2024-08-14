
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

##https://www.youtube.com/watch?v=-O2YuS0n03U&list=PLo9Vi5B84_dfAuwJqNYG4XhZMrGTF3sBx

### Python Dotenv
import os
from dotenv import load_dotenv

load_dotenv(override=True)  ## override=True, if want to override system wide env variable

API_KEY = os.getenv("API_KEY")
USERNAME = os.getenv("USERNAME")
ADDRESS = os.getenv("ADDRESS")
US = os.getenv("MAIL")
# print(API_KEY)
# print(USERNAME)
# print(ADDRESS)
print(US)
