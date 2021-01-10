# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# name 프로퍼티를 가진 Student를 부모 클래스로 major 프로퍼티를 가진 GraduateStudent 자식 클래스를 정의하고 
# 이 클래스의 객체를 다음과 같이 문자열로 출력하는 코드를 작성하십시오.

class Student() :
    def __init__(self, name) :
        self.__name = name
    
    @property
    def name(self) :
        return self.__name
    
    def __repr__(self):
        return f'이름: {self.name}'

class GraduateStudent(Student) :
    def __init__(self, major, new_name):
        Student.__init__(self, new_name)
        self.__major = major
    
    @property
    def major(self) :
        return self.__major

    def print_info(self) :
        print(f'이름: {self.name}, 전공: {self.major}')
    
S = Student('홍길동')
GS = GraduateStudent('컴퓨터', '이순신')
print(S)
GS.print_info()