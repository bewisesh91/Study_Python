# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 반지름 정보를 갖고, 원의 면적을 계산하는 메서드를 갖는 Circle 클래스를 정의하고, 생성한 객체의 원의 면적을 출력하는 프로그램을 작성하십시오.

class Circle():
    def __init__(self, r) :
        self.__r = r
    
    @property
    def r(self) :
        return self.__r
    
    @property
    def area(self) :
        return f'{3.14 * self.r ** 2}'

    def __repr__(self) :
        return f'원의 면적: {self.area}'

user_input = 2
result = Circle(user_input)
print(result)