# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1, 1 << 12):
        bitCnt = sum = 0
        for j in range(12):
            if i & (1 << j):
                sum += j+1
                bitCnt += 1
        if sum == K and bitCnt == N:
            cnt += 1
    print('#{0} {1}'.format(t+1, cnt))