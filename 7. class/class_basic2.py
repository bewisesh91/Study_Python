# 객체 지향의 이해
# 객체 지향 프로그래밍이란?
# 객체 형성(상태와 행위로 이루어짐) => 객체 조립 => 프로그램 형성
# 즉, 객체를 이용해 문제를 해결하려는 프로그래밍 방법

# 객체란?
# 변수와 메서드
# 변수는 값을 가지며, 메서드는 실행할 코드를 가짐
# 변수와 메서드가 서로 연관된 것들끼리 묶어 만든 것

# ex) 자동차
# 변수 : 연료량, 속도계
# 메서드 : 주행기능
# 메서드는 변수에 영향을 줌, 변수와 연관된 기능을 메서드라고 할 수 있음
# 서로 연관된 변수와 메서드를 잘 파악하고 묶어 객체를 형성하는 것이 중요

# 객체는 부품화가 가능하고 재사용성을 가짐
# Class는 객체를 만들기 위한 청사진, 설계도, 템플릿
# 같은 문제 도메인에 속하는 속성과 행위를 정의
# 객체 지향 프로그램의 기본적인 사용자 정의 데이터 타입

# instance는 메모리에 로딩된 클래스를 통해 클래스를 템플릿으로 하여 메모리 상에 생성된 정보
# 자신 고유의 속성을 가지며 클래스에서 정의한 행위 수행
# 인스턴스의 행위는 클래스에서 정의된 행위에 대한 정의를 공유함으로써 메모리를 효율적으로 사용

# 메서드는 클래스로부터 생성된 객체(인스턴스) 사용 시 객체에 명령을 내리는 행위
# 객체가 가지고 있는 메서드를 호출한다, 객체에 메시지를 전달한다라고 표현함
# 한 객체의 속성을 조작할 목적으로 사용
# 객체 간의 통신은 메시지 전달을 통해 이루어짐

# 객체 지향 프로그램의 특징
# 추상화, 상속, 다형성

# 추상화란? 객체에서 공통된 속성과 행위를 추출하는 것
# ex) 홍길동, 이순신, 강감찬 => 학생
# 공통 속성 : 학번, 이름, 주민번호, 학과, 주소, 전화번호
# 공통 행위 : 수강 신청하기, 휴학 신청하기, 복학 신청하기 등
# 공통의 속성과 행위를 찾아서 타입을 정의하는 과정

# 추상 데이터 타입
# 데이터 타입의 표현과 연산을 캡슐화, 접근 제어를 통해 데이터의 정보를 은닉할 수 있음
#  래스, 추상 데이터 타입의 인스턴스 : 객체, 추상 데이터 타입에서 정의된 연산 : 메서드

# 상속이란? 새로운 클래스가 기존의 클래스의 데이터와 연산을 이용할 수 있게 하는 기능
# 기존의 클래스 : 부모 클래스, 기반 클래스, 상위 클래스, 슈퍼 클래스
# 새로운 클래스 : 자식 클래스, 파생 클래서, 하위 클래스, 서브 클래스
# 하위 클래스를 이용해 프로그램의 요구에 맞추어 클래스 수정 가능
# 클래스 간의 종속 관계를 형성하여 객체 조직화 가능
# 상속을 하면 재사용으로 인해 코드가 줄어들고, 범용적인 사용 가능, 자료와 메서드의 자유로운 사용 및 추가 가능

# 다형성이란? 다양한 형태로 나타날 수 있는 특징
# 하나의 클래스 내부에 같은 이름의 행위를 여러개 정의하거나 상위클래스의 행위를 하위 클래스에서 재정의 가능
# 즉, 어떤 한요소에 여러 개념을 넣어 놓는 것
# 오버라이딩 : 같은 이름의 메서드가 여러 클래스에서 다른 기능을 하는 것
# 오버로딩 : 같은 이름의 메서드가 인자의 개수나 자료형에 따라서 다른 기능을 하는 것

# 메서드 오버라이딩 : 상속으로 물려 받은 재료나 메서드를 그대로 사용하지 않고 하위 클래스에서 새로 정의해 사용하는 기법
# 상위 클래스의 메서드와 동일한 서명(매개변수의 타입, 개수, 리턴 타입)을 가져야함

# 메서드 오버로딩 : 클래스 내부에 동일한 이름의 행위를 여러 개 정의하는 기법
# 메서드의 이름이 같고 매개변수의 타입과 수는 서로 달라야 함, 리턴 타입은 관계하지 않음
# 메서드 이름을 하나로 통일 가능하며, 같은 이름의 메서드에 여러 종류의 매개 변수를 받을 수 있음

members = [
    {"name" : "홍길동", "age" : 20},
    {"name" : "이순신", "age" : 45},
    {"name" : "강감찬", "age" : 35},
]

def create(name, age) :
    return {'name' : name, 'age' : age}

def to_str(person) :
    return f"{person['name']}\t{person['age']}"

members = [
    create('홍길동', 20),
    create('이순신', 45),
    create('강감찬', 35)
]

for member in members :
    print(to_str(member))

# 클래스 정의
# 클래스란? 객체 생성을 위한 청사진 또는 템플릿
# ex) 멤버와 관련된 추상 데이터 타입이 필요하다면
# 멤버 클래스 설계 => 멤버 클래스 제작 => 객체 생성 

# 클래스 정의 및 객체 생성
# 클래스 정의
# class 클래스명 :
# ...

# 객체 생성
# 변수 = 클래스명(), <- 이를 생성자 메서드라고하며 클래스 이름과 동일한 메서드이다.

class Person :
    pass

member = Person() # member 객체를 생성하는 Person()를 생성자 메서드라고 함

if isinstance(member, Person) : # True
    print('member는 Person 클래스의 인스턴스입니다.')

# 생성자 메서드 : 객체를 생성하기 위해 호출
# class 클래스명 :
# def __init__(self, 매개변수 목록) :
# ...

# 소멸자 메서드 : 객체가 소멸되기 전에 호출
# class 클래스명 :
# def __del__(self) :
# ...

# self는 객체 공간을 가르키는 식별자, 객체 공간의 필드와 메서드에 접근할 경우 self.식별자 형식 이용

class Person2 :
    def __init__(self, name, age) : # self가 가리키는 객체 공간에 name, age 필드 생성
        self.name = name
        self.age = age
        print(f'{self.name} 객체가 생성되었습니다.')
    
    def __del__(self) :
        print(f'{self.name} 객체가 제거되었습니다.')

member = Person2('홍길동', 20)
print(f'{member.name}\t{member.age}')
print(dir(member))

# 클래스와 인스턴스의 특징
# 인스턴스 메서드란? 
# self가 가리키는 객체의 필드 정보에 접근해 특정 목적의 기능을 수행하도록 정의된 메서드

class Person3 :
    def __init__(self, name, age) : # self가 가리키는 객체 공간에 name, age 필드 생성
        self.name = name
        self.age = age
        print(f'{self.name} 객체가 생성되었습니다.')
    
    def __del__(self) :
        print(f'{self.name} 객체가 제거되었습니다.')

    # 인스턴스 메서드
    def to_str(self) : 
        return f'{self.name}\t{self.age}'

members = [
    Person3('홍길동', 20),
    Person3('이순신', 45),
    Person3('강감찬', 35)
    ] 

for member in members:
    print(member.to_str()) # 인스턴스.메서드

# 인스턴스 변수란?
# 클래스 내에서 self.변수 형태를 가지는 변수
# 객체마다 가지고 있는 객체 고유의 정보

# 인스턴스 변수의 접근 제한 기능
class Person4 :
    def __init__(self, name, age) : 
        self.__name = name # __를 통해 프라이빗 필드 생성
        self.__age = age
        print(f'{self.__name} 객체가 생성되었습니다.')
    
    def __del__(self) :
        print(f'{self.__name} 객체가 제거되었습니다.')

    def to_str(self) :
        return f'{self.__name}\t{self.__age}'

    # 인스턴스 변수의 접근 제한 기능
    # member[0][1] = -200 이렇게 바꾸는 것을 막고, 아래의 인스턴스 변수를 사용하도록 지정
    def get_name(self) :
        return self.__name
    
    def get_age(self) :
        return self.__age

    def set_age(self, age) : # __age 필드의 값을 변경하는 메서드
        if age < 0 :
            raise TypeError('나이는 0이상의 값만 허용합니다.')
        self.__age = age





# members = [
#     Person4('홍길동', 20),
#     Person4('이순신', 45),
#     Person4('강감찬', 35)
# ]

# members[0].set_age(-20)

# for member in members :
#     print(member.to_str())


# 데코레이터 기능
# 변수 이름과 같은 메서드를 만들어 사용 가능
# class 클래스명 :
# ...
#       @property
#       def name(self) :

# class 클래스명 :
# ...
#       @property의이름.setter
#       def name(self) :

class Person5 :
    def __init__(self, name, age) : 
        self.__name = name # __를 통해 프라이빗 필드 생성
        self.__age = age
        print(f'{self.__name} 객체가 생성되었습니다.')
    
    def __del__(self) :
        print(f'{self.__name} 객체가 제거되었습니다.')

    def to_str(self) :
        return f'{self.__name}\t{self.__age}'
    
    @property # 모습은 메서드이지만,
    def name(self) : # 변수 처럼 사용 가능
        return self.__name # __name 필드 값을 반환하는 getter 메서드의 역할

    @property
    def age(self) :
        return self.__age
    
    @age.setter
    def age(self, age) :
        if age < 0:
            raise TypeError('나이는 0이상의 값만 허용합니다.')
        self.__age = age

members = [
    Person5('홍길동', 20),
    Person5('이순신', 45),
    Person5('강감찬', 35)
]

members[0].age = 55 # 메서드 처럼 age() 이렇게 안쓰고, age만 써도 된다.

for member in members :
    print(member.to_str())



# 클래스 변수
# 클래스 내에서 클래스명.변수 형식으로 선언된 변수
# 클래스 변수 정의 
# class 클래스명 :
#   클래스변수 = 값
#   ...
# 클래스 변수 접근
# 클래스명.클래스변수

class Person6:
    count = 0

    def __init__(self, name, age) : 
        self.__name = name # __를 통해 프라이빗 필드 생성
        self.__age = age
        Person6.count += 1 # 클래스 변수
        print(f'{self.__name} 객체가 생성되었습니다.')
    
    def to_str(self) :
        return f'{self.__name}\t{self.__age}'
    
    def __del__(self) :
        print(f'{self.__name} 객체가 제거되었습니다.')
        
    @property
    def name(self) : # 변수 처럼 사용 가능
        return self.__name # __name 필드 값을 반환하는 getter 메서드의 역할

    @property
    def age(self) :
        return self.__age
    
    @age.setter
    def age(self, age) :
        if age < 0:
            raise TypeError('나이는 0이상의 값만 허용합니다.')
        self.__age = age

people = [
    Person6('홍길동', 20),
    Person6('이순신', 45),
    Person6('강감찬', 35)
]

print(f'현재 Person6 클래스의 인스턴스는 총 {Person6.count}개 입니다.')

# 클래스 메서드
# 클래스가 소유한 메서드
# class 클래스명:
#   ...
#   @classmethod
#   def 클래스메서드(cls, 매개변수목록) :
#        ...

# 클래스 메서드의 사용
# 클래스명.클래스메서드(매개변수목록)

class Person7:
    count = 0

    def __init__(self, name, age) : 
        self.__name = name # __를 통해 프라이빗 필드 생성
        self.__age = age
        Person7.count += 1
        print(f'{self.__name} 객체가 생성되었습니다.')
    
    def to_str(self) :
        return f'{self.__name}\t{self.__age}'
    
    def __del__(self) :
        print(f'{self.__name} 객체가 제거되었습니다.')


    @property
    def name(self) : # 변수 처럼 사용 가능
        return self.__name # __name 필드 값을 반환하는 getter 메서드의 역할

    @property
    def age(self) :
        return self.__age
    
    @age.setter
    def age(self, age) :
        if age < 0:
            raise TypeError('나이는 0이상의 값만 허용합니다.')
        self.__age = age
    
    @classmethod # 클래스 메서드
    def get_info(cls) :
        return f'현재 Person7 클래스의 인스턴스는 총 {cls.count}개입니다.' # cls.count는 Person7.count와 동일

people = [
    Person7('홍길동', 20),
    Person7('이순신', 45),
    Person7('강감찬', 35)
]

print(Person7.get_info())



# 연산자 오버로딩
class Person8:
    count = 0

    def __init__(self, name, age) : 
        self.__name = name # __를 통해 프라이빗 필드 생성
        self.__age = age
        Person8.count += 1
        print(f'{self.__name} 객체가 생성되었습니다.')
    
    def to_str(self) :
        return f'{self.__name}\t{self.__age}'

    def __del__(self) :
        print(f'{self.__name} 객체가 제거되었습니다.')

    @property
    def name(self) : # 변수 처럼 사용 가능
        return self.__name # __name 필드 값을 반환하는 getter 메서드의 역할

    @property
    def age(self) :
        return self.__age
    
    @age.setter
    def age(self, age) :
        if age < 0:
            raise TypeError('나이는 0이상의 값만 허용합니다.')
        self.__age = age
    
    @classmethod
    def get_info(cls) :
        return f'현재 Person8 클래스의 인스턴스는 총 {cls.count}개입니다.'
    
    def __gt__(self, other) :
        return self.__age > other.__age
    
    def __ge__(self, other) :
        return self.__age >= other.__age
    
    def __lt__(self, other) :
        return self.__age < other.__age
    
    def __le__(self, other) :
        return self.__age <= other.__age

    def __eq__(self, other) :
        return self.__age == other.__age
    
    def __ne__(self, other) :
        return self.__age != other.__age

members = [
    Person8('홍길동', 20),
    Person8('이순신', 45),
    Person8('강감찬', 35)
]

cnt = len(members)
i = 0
while True :
    print(f'members[{i}] > members[{i+1}] => {members[i] > members[i + 1]} ')
    i += 1
    if i == cnt -1 :
        print(f'members[{i}] > members[{0}] => {members[i] > members[0]}')
        break

# 스트링 메서드 : __str()__
# str() 함수에 객체를 전달해 문자열로 변환
class Person9:
    count = 0

    def __init__(self, name, age) : 
        self.__name = name # __를 통해 프라이빗 필드 생성
        self.__age = age
        Person9.count += 1
        print(f'{self.__name} 객체가 생성되었습니다.')
    
    def to_str(self) :
        return f'{self.__name}\t{self.__age}'

    def __del__(self) :
        print(f'{self.__name} 객체가 제거되었습니다.')

    
    @property
    def name(self) : # 변수 처럼 사용 가능
        return self.__name # __name 필드 값을 반환하는 getter 메서드의 역할

    @property
    def age(self) :
        return self.__age
    
    @age.setter
    def age(self, age) :
        if age < 0:
            raise TypeError('나이는 0이상의 값만 허용합니다.')
        self.__age = age
    
    @classmethod
    def get_info(cls) :
        return f'현재 Person9 클래스의 인스턴스는 총 {cls.count}개입니다.'
    
    def __gt__(self, other) :
            return self.__age > other.__age
    
    def __ge__(self, other) :
        return self.__age >= other.__age
    
    def __lt__(self, other) :
        return self.__age < other.__age
    
    def __le__(self, other) :
        return self.__age <= other.__age

    def __eq__(self, other) :
        return self.__age == other.__age
    
    def __ne__(self, other) :
        return self.__age != other.__age

    def __str__(self) :
        return f'{self.__name}\t{self.__age}'

members = [
    Person9('홍길동', 20),
    Person9('이순신', 45),
    Person9('강감찬', 35)
]

for member in members :
    print(str(member)) # Person9 클래스의 객체 전달하면 __srt__ 메서드 호출


# 클래스 상속
# 부모 클래스의 동작을 자식 클래스가 재사용, 확장, 수정 하는 것을 의미
# class 클래스명(부모 클래스명) :

class Parent: # 부모 클래스
    def __init__(self, family_name) :
        self.__family_name = family_name
        print('Parent 클래스의 __init__() ...')
    
    @property
    def family_name(self) :
        return self.__family_name

class Child(Parent): # 자식 클래스
    def __init__(self, first_name, last_name) :
        Parent.__init__(self, last_name) # 부모 클래스의 __famil_name 필드를 매개변수 last_name으로 초기화
        # super().__init__(last_name) # Parent 대신 super()라고 작성해도 됨
        self.__first_name = first_name
        print('Child 클래스의 __init__() ...')
        
    @property
    def first_name(self) :
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
    
    @property
    def name(self) :
        return f'{self.family_name} {self.first_name}'
    
child = Child("길동", "홍")
print(child.family_name)
print(child.first_name)
print(child.name)
print('======>')
child.first_name = '길순'
print(child.name)

# 메서드 오버라이딩
# 부모 클래스에 있는 메서드와 동일한 서명을 가진 메서드를 자식 클래스에서 다시 정의해 사용하는 것

class Parent2:
    def __init__(self, family_name) :
        self.__family_name = family_name
        print('Parent2 클래스의 __init__() ...')
    
    @property
    def family_name(self) :
        return self.__family_name

    def print_info(self) :
        print(f'Parent2 : {self.family_name}')

class Child2(Parent2):
    def __init__(self, first_name, last_name):
        Parent2.__init__(self, last_name)
        self.__first_name = first_name
        print('Child2 클래스의 __init__() ...')

    @property
    def first_name(self) :
        return self.first_name
    
    @first_name.setter
    def first_name(self, first_name) :
        self.__first_name = first_name
    
    @property
    def name(self) :
        return f'{self.family_name} {self.first_name}'
    
    def print_info(self) :
        Parent2.print_info(self) # 메서드 오버라이딩
        print(f'Child2 : {self.name}')

child = Child2('길동', '홍')
child.print_info()
