# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고 메서드를 호출하는 코드를 작성해봅시다.

class Korean():
    def __init__(self, nation) :
        Korean.nation = nation
    
    @classmethod
    def printNationality(cls) :
        print(f'{cls.nation}')
        return f'{cls.nation}'

nationality = Korean('대한민국')
print(nationality.printNationality())