# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 주어진 튜플 (1,2,3,4,5,6,7,8,9,10)의 앞 항목 절반과 뒤 항목 절반을 출력하는 프로그램을 작성하십시오.


data = (1,2,3,4,5,6,7,8,9,10)

result1 = tuple([i for i in data if i < 6])
result2 = tuple([i for i in data if i > 5])
print(result1)
print(result2)
