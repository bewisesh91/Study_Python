# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.


num_input = input().split(",")
result1 = [int(i) for i in num_input]
result2 = tuple([int(i) for i in num_input])
print(result1)
print(result2)