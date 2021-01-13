# 2차원 리스트

### 2차원 리스트란?
# 1차원 리스트를 묶어놓은 리스트
# 2차원 리스트의 선언 : 세로길이(행이 개수), 가로길이(열의 개수)를 필요로 함
# ex) 2행 4열의 2차원 리스트 : list = [[0,1,2,3],[4,5,6,7]]

### 2차원 리스트 초기화
arr = [0, 0, 0, 0, 0]
arr = [0] * 5
arr = [i for i in range(2, 9) if i % 2 ==0]

brr = [[1, 2, 3], [1, 2, 3]]
brr = [[1, 2, 3] * 3]
brr = [[1, 2, 3] for i in range(3)]
brr = [[i, j] for i in range(3) for j in range(2)]

### 2차원 리스트 입력
# 3 4         첫째 줄에 n행 m열
# 0 1 0 0     둘째 줄부터 n * m의 행열 데이터가 주어질 경우 
# 0 0 0 0
# 0 0 1 0

# 방법 1
n, m = map(int, input().split())
mylist = [0 for _ in range(n)]
# mylist = [0]*n

for i in range(n) :
    mylist[i] = list(map(int, input().split()))

# 방법 2
n, m = map(int, input().split())
mylist = []
for i in range(n) :
    mylist.append(list(map(int, input().split())))

# 방법 3
n, m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(3)]

# 주어진 데이터에서 1이 입력된 [행, 열]의 위치 찾기
# 방법 1
n, m = map(int, input().split())
mylist = []
newlist = []
for i in range(n) :
    mylist.append(list(map(int, input().split())))
    for j in range(m) :
        if mylist[i][j] == 1 :
            newlist.append([i,j])

# 방법 2
n, m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(n)]
newlist = [(i,j) for i in range(n) for j in range(m) if mylist[i][j] == 1]


### 2차원 리스트 순회
# n x m 리스트의 n x m개의 모든 원소를 빠짐없니 조사하는 방법

arr = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
n = len(arr) # 행의 개수
m = len(arr[0]) # 열의 개수

# 행 우선 순회
for i in range(len(arr)) :
    for j in range(len(arr[i])) :
        arr[i][j]

# 열 우선 순회
for j in range(len(arr[0])) :
    for i in range(len(arr)) :
        arr[i][j]

# 지그재그 순회
for i in range(len(arr)) :
    for j in range(len(arr[0])) :
        arr[i][j + (m - 1 - 2 * j) * (i % 2)]


### 2차원 리스트 탐색
# 델타를 이용한 2차원 리스트 탐색
# 2차원 리스트의 한 좌표에서 네 방향의 인접 리스트 요소를 탐색할 때 사용하는 방법
# 델타 값은 한 좌표에서 네 방향의 좌표와 x, y의 차이를 저장한 리스트로 구현
# 델타 값을 이용하여 특정 원소의 상하좌우에 위치한 원소에 접근할 수 있음
# 2차원 리스트의 가장자리 원소들은 상하좌우, 네 방향에 원소가 존재하지 않을 경우가 있으므로, index를 체크하거나 index의 범위를 제한해야 함

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# (1, 1)에서 상은 (0, 1) 즉, x축은 변화 없고, y축만 -1
# (1, 1)에서 하는 (2, 1) 즉, x축은 변화 없고, y축만 +1
# (1, 1)에서 좌는 (1, 0) 즉, x축은 -1, y축은 변화 없음
# (1, 1)에서 우는 (1, 2) 즉, x축은 +1, y축은 변화 없음

for x in range(len(arr)) :
    for y in range(len(arr[x])) :
        for i in range(4) :
            testX = x + dx[i]
            testy = y + dy[i]
            print(arr[testX][testy])

### 전치 행렬
# 행과 열의 값이 반대인 행렬
arr = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
for i in range(3) :
    for j in range(3) :
        if i < j :
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)

# zip 함수 : 동일한 개수로 이루어진 자료형들을 튜플 객체로 묶어 주는 함수
alpha = ['a', 'b', 'c']
index = [1, 2, 3]
result = list(zip(alpha, index)) # [('a', 1), ('b', 2), ('c', 3)]

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(zip(*arr))) # 이렇게 zip(*matrix)를 사용하면 전치 행렬이 나온다


### 부분 집합
# 부분 집합의 합
# 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분 집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 확인하는 문제
# ex) {-7, -3, -2, 5, 8} 중 {-3, -2, 5}는 부분 집합이면서 모두 더한 값이 0이 되는 경우
# 완전 검색기법으로 부분 집합 합 문제를 풀 경우, 집합의 모든 부분 집합을 생성한 후 각 부분 집합의 합을 계산

# 부분 집합의 수
# 어떤 집합의 부분 집합을 구할 경우, 부분 집합의 총 개수는?
# 집합의 원소가 n개일 때, 공집합을 포함한 부분 집합의 수는 2의 n제곱 개

arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]
for i in range(2) :
    bit[0] = i                   # 0번째 원소
    for j in range(2):           
        bit[1] = j               # 1번째 원소
        for k in range(2):
            bit[2] = k           # 2번째 원소
            for l in range(2) :
                bit[3] = l       # 3번째 원소
                print(bit)

# bit [0, 0, 0, 0]은 공집합
# bit [0, 0, 0, 1]은 {4}
# bit [0, 0, 1, 0]은 {3}
# bit [0, 0, 1, 1]은 {3, 4}
# bit [0, 1, 0, 0]은 {2}

# 비트 연산자
# &(and) : 0011 & 0101 => 0001
# |(or) : 0011 | 0101 => 0111
# << : 3 << 2 => 0011을 1100으로 바꾸는 것, 즉 왼쪽 것을 2만큼 왼쪽으로 옮기라는 뜻 
# >> : 8 >> 2 => 0100을 0001으로 바꾸는 것, 즉 왼쪽 것을 2만큼 오른쪽으로 옮기라는 뜻

arr = [1, 2, 3]
n = len(arr) # 원소의 개수

for i in range(1<<n) : # 1<<n : 모든 부분 집합의 개수
    for j in range(n) : 
        if i & (1<<j) : # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end="")
    print()


### 검색
# 검색이란?
# 저장되어 있는 자료 중에서 원하는 항목(목적하는 탐색키를 가진 항목)을 찾는 작업 

# 검색의 종류
# 1) 순차 검색
# 일렬로 되어 있는 자료를 순서대로 검색하는 방법
# 리스트나 연결 리스트 등 순차구조로 구현된 자료구조에 유용함
# 구현이 쉽지만, 검색 대상이 많은 경우 수행시간의 증가로 비효율적임

## 정렬되지 않은 자료의 검색 과정
# 첫 번째 원소부터 순서대로 검색대상과 키 값이 같은 원소가 있는지를 비교하여 찾음
# 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환
# 자료구조의 마지막에 갈 때까지 검색 대상을 찾지 못하면 검색 실패

# ex) [4, 9, 11, 23, 2, 19, 7]
# 2를 검색하는 경우, 5번째에서 찾을 수 있음
# 8을 검색하는 경우, 검색 실패

# 찾고자 하는 원소의 순서에 따라 비교횟수가 결정됨
# 정렬되지 않은 자료에서의 순차 검색의 평균 비교 횟수 : 1/n * (1+2+...+n) = (n+1)/2
# 시간 복잡도 : O(n)

def sequentialSearch(lst, N, target) :
    i = 0
    while i < N and lst[i] != target :
        i += 1
    if i < N : 
        return i
    else :
        return -1

## 정렬된 자료의 검색 과정
# 자료가 오름차순으로 정렬된 상태의 경우
# 자료를 순차적으로 검색하면서 키 값을 비교함
# 원소의 키 값이 검색 대상의 키 값보다 크면 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료함

# ex) [2, 4, 7, 9, 11, 19, 23]
# 11을 검색하는 경우, 5번째에서 찾을 수 있음
# 10을 검색하는 경우, 5번째에서 검색 실패

# 정렬되어 있으므로, 검색 실패를 반환하는 경우 평균 비교 횟수가 반으로 줄어듦
# 시간 복잡도 : O(n)

def sequentialSearch2(lst, N, target) :
    i = 0
    while i < N and lst[i] < target :
        i += 1
    if i < N and lst[i] == target : 
        return i
    else :
        return -1


# 2) 이진 검색
# 자료의 가운데 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속하는 방법
# 목적 키를 찾을 때까지 이진 검색ㅇㄹ 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 빠르게 검색을 수행함
# 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 함
# 시간 복잡도 : O(logN)

## 이진 검색의 검색 과정
# 자료의 중앙에 있는 원소를 선택
# 중앙 원소의 값과 찾고자 하는 목표 값을 비교
# 목표값 < 중앙 원소 값 : 자료의 왼쪽 반에 대해서 새로 검색
# 목표값 > 중앙 원소 값 : 자료의 오른쪽 반에 대해서 새로 검색
# 목표 값을 찾을 때까지 반복

# ex) [2, 4, 7, 9, 11, 19, 23]
# 7을 검색하는 경우, 3번째에서 찾을 수 있음
# [2, 4, 7, 9, 11, 19, 23] 9기준 으로 검색
# [2, 4, 7] 4기준으로 검색
# [7] 검색 성공

# ex) [2, 4, 7, 9, 11, 19, 23]
# 20을 검색하는 경우, 검색 실패
# [2, 4, 7, 9, 11, 19, 23] 9기준 으로 검색
# 11, 19, 23] 19기준으로 검색
# [23] 검색 실패

# 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행함
# 이진 검색의 경우, 자료의 삽입이나 삭제가 발생하였을 때, 리스트의 상태를 정렬 상태로 유지하는 추가 작업이 필요

def binarySearch(lst, target) :
    start = 0
    end = len(lst) - 1
    while start <= end :
        middle = start + (end - start) // 2
        if target == lst[middle] :
            return True
        elif target < lst[middle] :
            end = middle - 1
        else :
            start = middle + 1
    return False

def binarySearch2(lst, low, high, target) :
    if low > high:
        return False
    else :
        middle = (low + high) // 2
        if target == lst[middle]:
            return True
        elif target < lst[middle]:
            return binarySearch2(lst, low, middle-1, target)
        elif target > lst[middle]:
            return binarySearch2(lst, middle+1, high, target)

# 인덱스
# 데이터베이스에서 유래, 테이블에 대한 동작 속도를 높임
# 인덱스는 키 필드만 갖고 있고 테이블의 다른 세부 항목은 갖고 있지 않음
# 이름 인덱스 리스트 : Name {Barbara, Florence, Melissa}, Original Index {1, 2, 0, 3}
# 원본 인덱스 리스트 : Name {Barbara, Florence, Melissa}, Number {429, 301, 302}, ID {aaa, bbb, ccc}, Original Index {1, 2, 0, 3}


### 정렬
# 셀렉션 알고리즘의 의미
# 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
# 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 함

# 셀렉션 선택 과정
# 정렬 알고리즘을 이용하여 자료를 정렬
# 원하는 순서에 있는 원소 가져오기

# k번째로 작은 원소를 찾는 알고리즘
# 1번부터 k번째까지 작은 원소들을 찾아 리스트의 앞쪽으로 이동시키고, 리스트의 k번째를 반환
# k가 비교적 작을 때 유용하며, O(kn)의 수행시간을 필요로 함
def select(lst, k) :
    for i in range(0, k) :
        minIndex = i
        for j in range(i+1, len(lst)):
            if lst[minIndex] > lst[j] :
                minIndex = j
        lst[i], lst[minIndex] = lst[minIndex], lst[i]
    return lst[k-1]

# ex) 포켓볼 순서대로 정렬하기
# 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

# 정렬 과정
# 주어진 리스트에서 최소값을 찾음
# 그 값을 리스트의 맨 앞에 위치한 값과 교환
# 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복
# 시간 복잡도 : O(n제곱)

# [64, 25, 10, 22, 11]
# 최소값을 찾음
# 리스트의 맨 앞에 위치한 값과 교환
# 미정렬 리스트에서 최소값을 찾음
# 리스트의 맨 앞에서 두번째 값과 교환
# 반복

# 선택 정렬 과정
def selectionSort(a) :
    for i in range(0, len(a)-1) :
        min = i 
        for j in range(i+1, len(a)) :
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]


