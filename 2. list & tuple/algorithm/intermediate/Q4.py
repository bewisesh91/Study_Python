# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# N개의 정수가 들어있는 배열에서 배열의 원소 중 이웃한 M개의 합을 계산하여 그 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하시오.

N = 10 # 10개의 정수
M = 3  # 이웃한 3개

N_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
New_list = []
for i in range(N-M+1) :
    New_list.append(sum(N_list[i:i+3]))

print(max(New_list)-min(New_list))
        