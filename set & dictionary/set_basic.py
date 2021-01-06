# 셋의 생성 및 조작법

# 셋이란? 
# 중괄호 {} 안에 서로 다른 자료형의 유일한 값을 콤마(,)로 구분해 하나 이상 저장할 수 있는 자료형
# 인덱스를 제공하지 않으며, 순서의 개념이 없고, 반복형 자료구조이나 데이터의 중복을 허용하지 않음

data_set = {10, 20, '파이썬', '파이썬'}
print(f'{type(data_set)}, {data_set}') # 중복을 허용하지 않아 문자열 '파이썬' 하나만 출력

data_str = 'better tomorrow'
data_set = set(data_str)
print(f'{type(data_set)}, {data_set}') # 정해진 순서 없이 출력, 중복 문자는 하나만 저장됨


# 셋 조작
# 셋 기본 연산
# 교집합 : &, intersection()
# 합집합 : |, union()
# 차집합 : -, difference()

data_set1 = {1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 7, 11}
data_set2 = {2, 3, 5, 9, 11, 12, 15}

print(f'{data_set1} & {data_set2} = {data_set1 & data_set2}')
print(f'{data_set1} | {data_set2} = {data_set1 | data_set2}')
print(f'{data_set1} - {data_set2} = {data_set1 - data_set2}')

# 셋 항목 추가
data_set = {1, 2, 3}
print(f'data_set : {data_set}')
data_set.add(4)
print(f'data_set : {data_set}')
data_set.update({5, 6, 7})
print(f'data_set : {data_set}')

# 셋 항목 제거
data_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f'data_set : {data_set}')
data_set.remove(4)
print(f'data_set : {data_set}')
data_set.pop()
print(f'data_set : {data_set}')
data_set.clear()
print(f'data_set : {data_set}')

# 셋 항목 확인
data_set1 = {1, 2, 3, 4, 5}
data_set2 = {2, 3}

print(f'3 in data_set1 => {3 in data_set1}')
print(f'6 not in data_set1 => {6 not in data_set1}')

print(f'{data_set1}.issuperset({data_set2}) => {data_set1.issuperset(data_set2)}')
print(f'{data_set2}.issubset({data_set1}) => {data_set2.issubset(data_set1)}')

# for 문을 이용한 셋 항목 접근
data_set = set(range(0, 11, 2))
for item in data_set :
    print(f'{item}', end = " ")

print()

for idx, item in enumerate(data_set) :
    print(f'[{idx}] => {item}')

# 셋 내포
data_set1 = {1, 2, 3, 4, 5}
print(f'data_set1 : {type(data_set1)}, {data_set1}')

data_set2 = {item for item in data_set1}
print(f'data_set2 : {type(data_set2)}, {data_set2}')

data_set3 = {item for item in data_set1 if item % 2 == 1}
print(f'data_set3 : {type(data_set3)}, {data_set3}')

data_set4 = {item for item in data_set1 if item % 2 == 0}
print(f'data_set4 : {type(data_set4)}, {data_set4}')

data_set5 = {x * y for x in data_set1 if x % 2 == 1
                    for y in data_set1 if y % 2 ==0 }
print(f'data_set5 : {type(data_set5)}, {data_set5}')