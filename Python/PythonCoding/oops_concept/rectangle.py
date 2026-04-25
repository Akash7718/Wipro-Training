from oops_concept.formulamethods import FM


class Rectangle(FM):
    def __init__(self, l,b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)