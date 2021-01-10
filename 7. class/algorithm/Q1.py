# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

class Value_Sum():
    def __init__(self, *args) :
        self.__values = []
        for arg in args :
            self.__value = arg
            self.__values.append(self.__value)
        self.__total_value = sum(self.__values)

    @property
    def total_value(self) :
        return self.__total_value

    def __repr__(self) :
        return f'국어, 영어, 수학의 총점: {self.total_value}'

total_value = Value_Sum(89, 90, 100)
print(total_value)