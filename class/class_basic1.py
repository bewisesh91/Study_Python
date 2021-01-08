# 클래스 생성 1
class Book(object) :
    def __init__(self, title, author) : # 생성자, 클래스를 선언할 때 인자로 받아올 것들을 정의
        self.title = title              # 생성자는 클래스를 사용하려 할 때 자동으로 호출되는 함수
        self.author = author            # 생성자 안에서 self.인자명 = 인자명 등으로 사용할 것들을 정의
    
    def print_title(self) :             
        print(self.title)               # self.인자명 으로 작성한 것들을 사용할 수 있음

    def print_author(self) :
        print(self.author)              # self.인자명 으로 작성한 것들을 사용할 수 있음
    
book1 = Book('오만과 편견', '제인오스틴')
print(book1.title)
print(book1.author)
book1.print_title()
book1.print_author()

# 클래스 생성 2
class Student(object) :
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender

    def birth_year(self) :
        now_year = 2021
        print(now_year - self.age + 1)

    def last_name(self) :
        print(self.name[0])

    def change_name(self, new_name) :
        self.name = new_name

student1 = Student('문승현', 31, 'Male')
student1.birth_year()
student1.last_name()

# 클래스 생성 3
class Supermarket(object) :
    def __init__(self, location, name, product, customer) :
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def printLocation(self) :
        print(self.location)
    
    def changeCategory(self, new_product) :
        self.product = new_product
    
    def showList(self) :
        print(self.product)
    
    def enterCustomer(self) :
        self.customer = self.customer + 1
    
    def showInfo(self) :
        print(self.name, self.location, self.product, self.customer)

supermarket1 = Supermarket('서울', 'S슈퍼마켓', '과자', 0)
supermarket1.printLocation()
supermarket1.changeCategory('아이스크림')
supermarket1.showList()
supermarket1.enterCustomer()
supermarket1.showInfo()

