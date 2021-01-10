# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환하는 프로그램을 작성하십시오.

user_input = input()

total = 0
for i in user_input :
    total = total + int(i)
print(total)