# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

num_input = input()

result = {x: x**2 for x in range(1, int(num_input)+1)}
print(result)