# _*_ coding: utf-8 _*_

class Student() :
    def __init__(self, name, gender, height) :
        self.__name = name
        self.__gender = gender
        self.__height = height
    
    # 읽기만 가능한 property 생성
    @property
    def name(self) :
        return self.__name
    
    @property
    def gender(self) :
        return self.__gender
    

    # 읽고 쓰기가 가능한 property 생성
    @property
    def height(self) :
        return self.__height

    @height.setter
    def height(self, height) :
        self.__height = height
    

    def __repr__(self) :
        return f'{self.__class__.__name__} (name : {self.name}, gender : {self.gender}, height : {self.height})'
        # 클래스의 이름(name : , gener : , height :) 이런 식으로 출력
        # repr을 str로 바꾸어도 동일하게 출력 됨
    
# s1 = Student('홍길동', '남', 176.5)
# print(s1)

students = [
    Student('홍길동', '남', 176.5),
    Student('이순신', '남', 188.5),
    Student('유관순', '여', 158.4),
    Student('강감찬', '남', 182.2)
]

print('"name"으로 오름차순 정렬 후 ===>')
# sorted 함수는 반복가능한 객체를 대상으로 사용 가능
# 사용자 정의 객체 사용 시 키로 사용할 정보를 전달해야 함
# 이때, lambda 함수를 사용하는데, lambda 함수의 x 값에는 반복가능한 객체의 값이 들어감
for student in sorted(students, key = lambda x : x.name) : 
    print(student)

print('"name"으로 내림차순 정렬 후 ===>')
for student in sorted(students, key = lambda x : x.name, reverse=True) : 
    print(student)

print('"height"으로 오름차순 정렬 후 ===>')
for student in sorted(students, key = lambda x : x.height) : 
    print(student)