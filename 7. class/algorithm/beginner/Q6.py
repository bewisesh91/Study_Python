# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

class Shape() :
    def area(self) :
        return 0

class Square(Shape) :
    def __init__(self, length) :
        Shape.__init__(self)
        self.__length = length
    
    @property
    def length(self) :
        return self.__length
    
    @property
    def area(self) :
        return self.length * self.length
    
    def __repr__(self) :
        return f'정사각형의 면적: {self.area}'

result = Square(3)
print(result)