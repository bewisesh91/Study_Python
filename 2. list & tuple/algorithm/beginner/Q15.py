# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

user_input = sorted(list(input().split(", ")))
print(user_input)

result = ""
for i in user_input :
    result += i + ", "
print(result[0:-2])