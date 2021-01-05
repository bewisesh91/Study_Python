# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

user_input = list(map(int, input().split(",")))

num_lists = []
for i in range(user_input[0]) :
    num_list = [i * j for j in range(user_input[1])]
    num_lists.append(num_list)
print(num_lists)