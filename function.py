import mod
import math

def greeting():
    print("Hello world")

greeting()

#Parameter functions
def add(a,b):
    add1 = a + b
    print(add1)

add(1,3)

#Return functions
def multi(a,b):
    return a*b

value = multi(2,4)
print(value)

#Default value function paramater
def username(name="Enter Your Name"):
    print(name)

username()

mod.show()

def div(a):
    print(math.sqrt(a))

div(5)