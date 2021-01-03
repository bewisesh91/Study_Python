# 튜플의 생성 및 조작법

# 튜플이란? 
# 괄호 () 안에 서로 다른 자료형의 값을 콤마(,)로 구분하여 하나 이상 저장할 수 있는 자료형
# 개별 항목은 0부터 시작하는 인덱스를 이용하여 접근
# 저장된 항목은 변경 불가능, 리스트와 다른점


# 튜플 생성
data_tuple = (10, 21.5, "파이썬", True)
print(f'{type(data_tuple)}, {data_tuple}')

data_tuple = tuple(range(10, 21, 2))
print(f'{type(data_tuple)}, {data_tuple}')

data_tuple = tuple('안녕하세요')
print(f'{type(data_tuple)}, {data_tuple}')

# 투플 조작
# 튜플 항목 접근
data_tuple = (10, 20, 30, 40, 50)
print(f'data_tuple : {data_tuple}')
print(f'data_tuple[0] : {data_tuple[0]}')
print(f'data_tuple[1] : {data_tuple[1]}')
print(f'data_tuple[-1] : {data_tuple[-1]}')
print(f'data_tuple[0:3] : {data_tuple[0:3]}') # 시작 인덱스 : 종료 인덱스 => 이때, 종료 인덱스는 미포함 함(0, 1, 2)
print(f'data_tuple.index(20) : {data_tuple.index(20)}') # 해당 값이 들어 있는 첫 번째 위치의 인덱스 반환

# 튜플 기본 연산
data_tuple1, data_tuple2 = (10, 20, 30), (40, 50)
print(f'{data_tuple1} + {data_tuple2} => {data_tuple1 + data_tuple2}')
print(f'{data_tuple1} * 2 => {data_tuple1 * 2}')
print(f'{data_tuple2} * 3 => {data_tuple2 * 3}')

# 튜플 항목 확인
data_tuple = [10, 20, 30, 40, 50, 50, 70, 80]
print(f'50 in data_tuple => {50 in data_tuple}')
print(f'50 not in data_tuple => {50 not in data_tuple}')
print(f'data_tuple.count(50) => {data_tuple.count(50)}')
print(f'data_tuple.count(90) => {data_tuple.count(90)}')

# 튜플과 for문
data_tuple = tuple(range(0, 11, 2))

for item in data_tuple :
    print(f'{item}', end=" ")
print()
for idx, item in enumerate(data_tuple) :
    print(f'data_tuple[{idx}] => {item}')

# 튜플 내포
data_tuple1 = (1, 2, 3, 4, 5)
print(f'data_tuple1 : {type(data_tuple1)} {data_tuple1}')

data_generator1 = (item for item in data_tuple1)
print(f'data_generator1 : {type(data_generator1)}, {data_generator1}')

data_tuple2 = tuple(data_generator1)
print(f'data_tuple2 : {type(data_tuple2)} {data_tuple2}')

data_tuple3 = tuple(item for item in data_tuple1 if item % 2 == 1)
print(f'data_tuple3 : {type(data_tuple3)} {data_tuple3}')

data_tuple4 = tuple(item for item in data_tuple1 if item % 2 == 0)
print(f'data_tuple4 : {type(data_tuple4)} {data_tuple4}')

data_tuple5 = tuple(x * y for x in data_tuple1 if x % 2 == 1
                        for y in data_tuple1 if y % 2 == 0) 
print(f'data_tuple5 : {type(data_tuple5)} {data_tuple5}')

