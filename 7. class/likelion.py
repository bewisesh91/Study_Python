class Figure :
    def __init__(self, dots, height, width) :
        self.dots = dots
        self.height = height
        self.width = width
    
    def calcArea(self) :
        return int(self.height) * int(self.width)

class Line(Figure) :
    def calcArea(self) :
        return f'line의 점의 갯수 : {self.dots}, line의 넓이 : {int(self.height) * int(self.width) * 0}'

class Triangle(Figure) :
    def calcArea(self) :
        return f'triangle의 점의 갯수 : {self.dots}, triangle의 넓이 : {int(int(self.height) * int(self.width) * 0.5)}'

class Rectangle(Figure) :
    def calcArea(self) :
        return f'rectangle의 점의 갯수 : {self.dots}, rectangle의 넓이 : {int(self.height) * int(self.width)}'


line = Line(2, 4, 0)
print(line.calcArea())

triangle = Triangle(3, 4, 2)
print(triangle.calcArea())

rectangle = Rectangle(4, 4, 2)
print(rectangle.calcArea())