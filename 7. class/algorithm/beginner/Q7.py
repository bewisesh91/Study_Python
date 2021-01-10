# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

class Person() :
    def getGender(self) :
        return 'Unknown'

class Male(Person) :
    def __init__(self) :
        Person.__init__(self)

    def getGender(self) :
        return 'Male'

class Female(Person) :
    def __init__(self) :
        Person.__init__(self)

    def getGender(self) :
        return 'Female'


result1 = Male()
print(result1.getGender())
result2 = Female()
print(result2.getGender())