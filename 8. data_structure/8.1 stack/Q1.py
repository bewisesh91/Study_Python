# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.


test_case = int(input())
for t in range(test_case) :
    square = [1, 3]
    n = int(input())
    for i in range(2, n//10) :
        num = 2*square[i-2] + square[i-1]
        square.append(num)
    print(f'#{t+1} {square[i]}')