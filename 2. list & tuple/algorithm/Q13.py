# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아 이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.




import math
user_input = input()
num_list = list(map(int, user_input.split(",")))
result = ""
for i in num_list :
    result += f'{i*2*math.pi:0.2f}, ' 
print(result[0:-2])
