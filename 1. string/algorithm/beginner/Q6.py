# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 다음 결과와 같이 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램을 작성하십시오.

user_input = 'H1e2l3l4o5w6o7r8l9d'

result = ""
for i in range(len(user_input)) :
    if i % 2 == 0 :
        result += user_input[i]
print(result)