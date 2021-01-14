# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
# 짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.


def binarySearch(total, target) :
    start = 1
    end = total
    count = 0
    while start <= end :
        middle = (start + end) // 2
        count += 1
        if middle == target :
            return count
        elif target > middle :
            start = middle
        else :
            end = middle

test_case = int(input())
for i in range(test_case) :
    total, a, b = map(int, input().split(' '))
    A = binarySearch(total, a)
    B = binarySearch(total, b)
    if A > B :
        print(f'#{i+1} B')
    elif A < B :
        print(f'#{i+1} A')
    else :
        print(f'#{i+1} 0')
    

