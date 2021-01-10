# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 가로, 세로 정보을 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고, 생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.

class Rectangle() :
    def __init__(self, width, height) :
        self.__width = width
        self.__height = height
    
    @property
    def width(self) :
        return self.__width
    
    @property
    def height(self) :
        return self.__height
    
    @property
    def area(self) :
        return f'{self.width * self.height}'
    
    def __repr__(self) :
        return f'사각형의 면적 : {self.area}'

result = Rectangle(4, 5)
print(result)