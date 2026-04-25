from oops_concept.rectangle import Rectangle
from oops_concept.square import Square

sqobj = Square(10)

print(f'Area: {sqobj.area()} \t perimeter: {sqobj.perimeter()}')

recobj = Rectangle(l=10, b=5)
print(f'Area: {recobj.area()} \t perimeter: {recobj.perimeter()}')


