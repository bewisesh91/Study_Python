# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

test_case = int(input())

for t in range(test_case) :
    data = input()
    i = 0
    while True :
        if i == len(data) - 1 :
            break
        if data[i] == data[i+1] :
            data = data.replace(data[i], "")
            print(data)
            pass
        i += 1
    print(f'#{t+1} {len(data)}')

