# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다

N = 5
N_list = [7,7,9,7,9,4,6,5,4,3]

count = [0]*10

for i in N_list :
    count[i] += 1

max_count = 0
for i in range(len(count)):
    if count[i] >= max_count :
        max_count = count[i]
        max_index = i

print(max_index)
print(max_count)
