# 딕셔너리의 생성 및 조작법

# 딕셔너리란?
# 중괄호 {}안에 {키 : 값}의 형식을 가진 유일한 데이터를 콤마로 구분해 하나 이상 저장할 수 있는 자료형
# 인덱스를 제공하지 않음, 순서의 개념이 없음, 키의 중복을 허용하지 않음

# 딕셔너리의 생성
data_dict1 = {
    '홍길동' : 20,
    '이순신' : 45,
    '강감찬' : 35
}
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')

data_dict2 = dict(홍길동 = 20, 이순신 = 45, 강감찬 = 35)
print(f'data_dict2 : {type(data_dict2)}, {data_dict2}')

data_tuple = (('홍길동', 20), ('이순신', 45), ('강감찬', 35))
data_dict3 = dict(data_tuple)
print(f'data_dict3 : {type(data_dict3)}, {data_dict3}')

data_list = [('홍길동', 20), ('이순신', 45), ('강감찬', 35)]
data_dict4 = dict(data_list)
print(f'data_dict4 : {type(data_dict4)}, {data_dict4}')

data_set = {('홍길동', 20), ('이순신', 45), ('강감찬', 35)}
data_dict5 = dict(data_set)
print(f'data_dict5 : {type(data_dict5)}, {data_dict5}')

# 딕셔너리 항목 접근
data_dict1 = {
    '홍길동' : 20,
    '이순신' : 45,
    '강감찬' : 35
}
print(f'data_dict1["홍길동"] = > {data_dict1["홍길동"]}')

# 딕셔너리 조작법
# 딕셔너리 항목 추가
data_dict1 = {
    '홍길동' : 20,
    '이순신' : 45,
    '강감찬' : 35
}
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')

data_dict1['을지문덕'] = 40
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')

data_dict1.update({'심사임당' : 50, '유관순' : 16})
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')

# 딕셔너리 항목 변경
data_dict1 = {
    '홍길동' : 20,
    '이순신' : 45,
    '강감찬' : 35
}
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')

data_dict1['강감찬'] = 38
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')

data_dict1.update({'홍길동' : 30, '이순신' : 55})
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')

# 딕셔너리 항목 제거
data_dict1 = {
    '홍길동' : 20,
    '이순신' : 45,
    '강감찬' : 35,
    '을지문덕' : 40
}
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')

del data_dict1['강감찬']
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')

data_dict1.pop('이순신') 
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')

data_dict1.clear()
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')

# 딕셔너리 항목 확인
data_dict1 = {
    '홍길동' : 20,
    '이순신' : 45,
    '강감찬' : 35,
    '을지문덕' : 40
}
print(f'data_dict1 : {type(data_dict1)}, {data_dict1}')
print(f'"홍길동" in data_dict1 => {"홍길동" in data_dict1}')
print(f'"신사임당" not in data_dict1 => {"신사임당" not in data_dict1}')

