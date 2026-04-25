from oops_concept.formulamethods import FM

class Square(FM):
    def __init__(self,s):
        self.side = s

    def area(self):
        return self.side* self.side

    def perimeter(self):
        return 4 * self.side

