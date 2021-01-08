# 리스트의 생성 및 조작법

# 리스트란? 
# 대괄호 [] 안에 서로 다른 자료형의 값을 콤마(,)로 구분하여 하나 이상 저장할 수 있는 자료형
# 개별 항목은 0부터 시작하는 인덱스를 이용하여 접근
# 저장된 항목도 변경 가능


# 리스트 생성
data_list = [10, 21.5, "파이썬", True] 
print(f'{type(data_list)}, {data_list}')

data_list = list(range(10, 21, 2))
print(f'{type(data_list)}, {data_list}')

data_list = list('안녕하세요')
print(f'{type(data_list)}, {data_list}')


# 리스트 조작
# 리스트 항목 접근
data_list = [10, 20, 30, 40, 50]
print(f'data_list : {data_list}')
print(f'data_list[0] : {data_list[0]}')
print(f'data_list[1] : {data_list[1]}')
print(f'data_list[-1] : {data_list[-1]}')
print(f'data_list[0:3] : {data_list[0:3]}') # 시작 인덱스 : 종료 인덱스 => 이때, 종료 인덱스는 미포함 함(0, 1, 2)
print(f'data_list.index(20) : {data_list.index(20)}') # 해당 값이 들어 있는 첫 번째 위치의 인덱스 반환

# 리스트 기본 연산
data_list1, data_list2 = [10, 20, 30], [40, 50]
print(f'{data_list1} + {data_list2} => {data_list1 + data_list2}')
print(f'{data_list1} * 2 => {data_list1 * 2}')
print(f'{data_list2} * 3 => {data_list2 * 3}')

# 리스트 항목 추가
data_list = [10, 20, 30, 40]
print(f'{data_list}')

data_list.append(50)
data_list.append(60)
print(f'{data_list}')

data_list.insert(2, 20)
print(f'{data_list}')

data_list.extend([70, 80]) # 리스트 덧셈 연산과 유사
data_list.append([90, 100]) # 객체에 리스트를 항목으로 추가
print(f'{data_list}')

# 리스트 항목 변경
data_list = [10, 20, 30, 40]
data_list[3] = 70
print(f'{data_list}')

data_list[1:3] = [12, 15]
print(f'{data_list}')

data_list[1:3] = [12, 15, 20] # 전체 리스트 크기가 늘어남
print(f'{data_list}')

# 리스트 항목 제거
data_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
del data_list[2]
print(f'{data_list}')

del data_list[3:5]
print(f'{data_list}')

data_list.pop(5)
print(f'{data_list}')

data_list.remove(100)
print(f'{data_list}')

data_list.clear()
print(f'{data_list}')

# 리스트 항목 확인
data_list = [10, 20, 30, 40, 50, 50, 50, 80, 90, 100]
print(f'50 in data_list => {50 in data_list}')
print(f'50 not in data_list => {50 not in data_list}')

print(f'data_list.count(50) => {data_list.count(50)}')
print(f'data_list.count(60) => {data_list.count(60)}')

# 리스트와 for문
data_list = list(range(0, 11, 2))

for item in data_list :
    print(f'{item}', end=" ")
print()
for idx, item in enumerate(data_list) :
    print(f'data_list[{idx}] => {item}')

# 리스트 내포
data_list1 = [1, 2, 3, 4, 5]
print(f'data_list1 : {type(data_list1)} {data_list1}')

data_list2 = []
for item in data_list1 :
    data_list2.append(item)
print(f'data_list2 : {type(data_list2)} {data_list2}')

data_list3 = [item for item in data_list1]
print(f'data_list3 : {type(data_list3)} {data_list3}')

data_list4 = []
for item in data_list1 :
    if item % 2 == 1 :
        data_list4.append(item)
print(f'data_list4 : {type(data_list4)} {data_list4}')

data_list5 = [item for item in data_list1 if item % 2 == 1]
print(f'data_list5 : {type(data_list5)} {data_list5}')

data_list6 = [item for item in data_list1 if item % 2 == 0]
print(f'data_list6 : {type(data_list6)} {data_list6}')

data_list7 = []
for x in data_list1 :
    if x % 2 == 1 : # 1, 3, 5
        for y in data_list1 :
            if y % 2 == 0 : # 2, 4
                data_list7.append(x * y) # 1 * 2, 1 * 4, 3 * 2, 3 * 4, 5 * 2, 5 * 4
print(f'data_list7 : {type(data_list7)} {data_list7}')

data_list8 = [x * y for x in data_list1 if x % 2 == 1
                    for y in data_list1 if y % 2 == 0]
print(f'data_list8 : {type(data_list8)} {data_list8}')

data_list9 = [item.lower() for item in 'Hello Python']
print(f'data_list9 : {type(data_list9)} {data_list9}')
