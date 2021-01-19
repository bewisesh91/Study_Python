# stack
# 물건을 쌓아 올리듯 자료를 쌓아 오린 형태의 자료구조
# stack에 저장된 자료는 선형구조를 가짐
# 선형구조 : 자료 간의 관계가 1대 1의 관계를 가짐
# 비선형구조 : 자료 간의 관계가 1대 N의 관계를 가짐(ex tree)
# stack에 자료를 삽입하거나 stack에서 자료를 꺼낼 수 있음
# 마지막에 삽입한 자료를 가장 먼저 꺼냄
# 후입선출(LIFO, Last In Frist Out)

# stack 자료구조 구현
# 자료를 선형으로 저장할 저장소가 필요함
# 파이썬에서는 리스트를 사용할 수 있음
# 저장소 자체를 stack이라고 부르기도 함
# stack에서 마지막 삽입된 원소의 위치를 top이라고 부름

# stack 연산
# 삽입 : 저장소에 자료를 저장, 보통 push라고 부름
# 삭제 : 저장소에서 자료를 꺼냄, 꺼낸 자료는 삽입한 자료의 역순으로 꺼냄, 보통 pop이라고 부름
# isEmpty : stack이 공백인지 아닌지를 확인하는 연산
# peek : stack의 top에 있는 item을 반환하는 연산

# push 알고리즘
def push(item):
    s.append(item)

# pop 알고리즘
def pop() :
    if len(s) == 0 :
        print('stack is empty')
        return
    else :
        return s.pop(-1)
s = []
push(1)
push(2)
push(3)

print('pop item =>', pop())
print('pop item =>', pop())
print('pop item =>', pop())

# stack 응용
# 괄호 검사 알고리즘
# 문자열에 있는 괄호를 차례대로 조사
# ( 왼쪽 괄호가 나타나면 push, ) 오른쪽 괄호가 나타나면 pop 수행, 짝이 맞는지 확인

# 재귀 호출
# 자기 자신을 호출하여 순환 수행되는 것
# 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀 호출 방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성 가능

# ex) Factorial 구하기
# Factorial 함수에서 n=4인 경우의 실행
# Factorial(4) = 4 x Factorial(3) -> Factorial(3) = 3 x Factorial(2) -> Factorial(2) = 2 x Factorial(1) -> Factorial(1) = 1

# ex) 피보나치 수열
# 0과 1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열
# F0 = 0, F1 = 1
# Fi = F(i-1) + F(i-2)
def fibo(n) :
    if n < 2 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)

# Memoization(메모이제이션)
# 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
# DP(동적계획법)의 핵심이 되는 기술

def fibo1(n) :
    global memo
    if n >=2 and len(memo) <= n :
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]
memo = [0, 1]

# DP(동적계획법)
# Dynamic Programming의 약자
# 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘
# 먼저 입력 크기가 작은 부분 무제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결
# 최종적으로 원래 주어진 입력의 문제를 해결

# 피보나치 수를 구하는 함수에 DP 적용하기
# 문제를 부분 문제로 분할
# 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구함
# 그 결과는 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구함

def fibo2(n) :
    f = [0, 1]
    for i in range(2, n+1) :
        f.append(f[i-1] + f[i-2])
    return f[n]

# DP 구현 방식
# recursive 방식 : fibo1()
# iterative 방식 : fibo2()
# 피보나치수열의 경우 iterative 방식이 보다 효율적

# DFS(깊이 우선 탐색)
# 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요
# 그 방법으로 DFS(깊이 우선 탐색, Depth First Search), BFS(너비 우선 탐색, Breadth First Search)가 있음

# DFS 방법
# 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색
# 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아옴
# 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하여 순회
# 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로, 후입선출 구조의 stack을 사

# 시작 정점 v를 결정하여 방문
# 정점 v에 인접한 정점 중에서
# 방문하지 않은 정점 w가 있으면, 정점 v를 stack에 push하고 정점 w를 방문, w를 v로하여 다시 반복
# 방문하지 않은 정점 w가 없으면, 탐색의 방향을 바꾸기 위해서 stack을 pop하여 받은 가장 마지막 방문 정점을 v로하여 다시 반복

