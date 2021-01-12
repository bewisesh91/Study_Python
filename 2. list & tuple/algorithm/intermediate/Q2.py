# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

# test_case = 3

# case_1
# K, N, M = 3, 10 ,5(최대 이동 가능 거리, 종점, 충전기 정류장 수)
# M_list = 1 3 5 7 9(충전기 정류장 번호)

# test_case = int(input())
# K, N, M = map(int, input().split())
# M_list = list(map(int, input().split()))

test_case = 3
K, N, M = 3, 10, 5
M_list = [1, 3, 5, 7, 9]

M_station = [0]*(N+1) # 시작 0, 종점 10까지 총 11개
for num in M_list :
    M_station[num] += 1 # 충전기가 설치된 정류장 = 1, 아닌 정류장 = 0

print(f'충전기가 설치된 정류장 표시 : {M_station}')

start = 0 # 시작 0
able_move = K # 최대 이동 가능 지점 = 최대 이동 가능 거리
charge_count = 0 #충전 횟수

while True :
    no_mark = 0
    print(start, no_mark)
    for i in range(start + 1, able_move + 1) : # 첫 시행의 범위는 ragne(1, 4)
        if M_station[i] == 1 :
            start = i # 범위 내 마지막 충전소의 번호로 업데이트
        else :
            no_mark += 1
        print(start, no_mark)
    print('Done')

    if no_mark == able_move : # 충전 못하는 횟수가 최대 이동 가능 거리랑 같다면
        print('0')
        break

    charge_count += 1
    able_move = K + start # 새로운 최대 이동 가능 지점 = 최대 이동 가능 거리 + 마지막 충전 지점 

    if able_move >= N :
        break
    
print(f'{charge_count}')