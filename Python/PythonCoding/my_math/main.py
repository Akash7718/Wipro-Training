"""
importing user defined module
"""
from my_math.arithmetic import add,subtract,multiply,divide
from my_math.geometry import circle_area, rectangle_area

a=int(input("enter 1st no : "))
b=int(input("enter 2nd no : "))
r=float(input("enter radius : "))
l=int(input("enter length : "))
w=int(input("enter width : "))

print("Addition: ",add(a,b))
print("Subtraction: ",subtract(a,b))
print("Multiplication: ",multiply(a,b))
print("Division: ",divide(a,b))

print("Circle Area: ",circle_area(r))
print("Rectangle Area: ",rectangle_area(l,w))
