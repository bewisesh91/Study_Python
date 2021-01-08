# 문자열 연산

# 문자열 연결
# message = '안녕하세요'
# guest = '홍길동'

# gretting = guest + '님, ' + message
# print(gretting)

# # 문자열 반복
# print('='*40)
# print('-'*14, end="")
# print('문자열의 반복', end="")
# print('-'*13)
# print('='*40)

# # 문자열 선택
# data_str = '안녕하세요, 파이썬입니다.'

# idx = 0
# cnt = len(data_str)
# while True:
#     print(f'data_str[{idx}] : {data_str[idx]}')
#     if idx == cnt -1:
#         break
#     idx += 1

# print('-'*20)

# # 문자열의 범위 선택
# data_str = '와우! 안녕하세요, 파이썬입니다.'
# start = int(input('시작 인덱스를 입력하세요: '))
# end = int(input('종료 인덱스를 입력ㄷ하세요: '))

# print(f'{data_str[start : end]}')

# # 문자열 함수
# # 문자열의 출현 횟수
# data_str = 'Have a nice day'
# print(f'"{data_str}"')
# input_str = input('위에서 찾고자하는 문자열을 입력하세요 : ')
# print(f'"{data_str}"에서 "{input_str}"은(는) {data_str.count(input_str)}번 나타납니다.')

# # 문자열의 길이 
# data_str = 'Have a nice day'
# print(f'len()을 이용한 "data_str" 문자열의 길이 검사 : {len(data_str)}')

# # 문자열 찾기
# data_str = '파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다.'
# print(f'"{data_str}"')
# input_str = input('위에서 찾고자하는 문자열을 입력하세요 : ')

# idx = data_str.find(input_str) # 왼쪽에서부터 찾는다
# if idx != -1 : # 못찾을 경우 -1을 반환하기 때문에
#     print(f'\t"{input_str} : [{idx}]')
# else :
#     print(f'\t"{input_str}"를 찾을 수 없습니다.')

# idx = data_str.rfind(input_str) # 오른쪽에서부터 찾는다
# if idx != -1 : # 못찾을 경우 -1을 반환하기 때문에
#     print(f'\t"{input_str} : [{idx}]')
# else :
#     print(f'\t"{input_str}"를 찾을 수 없습니다.')

# try :
#     idx = data_str.index(input_str) # index의 경우 못찾을 경우 에러를 발생
#     print(f'\t"{input_str} : [{idx}]')
# except ValueError:
#     print(f'\t"{input_str}"를 찾을 수 없습니다.')

# 문자열의 삽입
# data_str = '가나다라마바사아자차카타파하'
# comma_space = ', '

# output = comma_space.join(data_str)
# print(f'{output}')

# # 대소문자 바꾸기
# data_str = 'better tomorrow'
# data_str = data_str.capitalize() 
# print(f'{data_str}')
# data_str = data_str.lower()
# print(f'{data_str}')
# data_str = data_str.upper()
# print(f'{data_str}')

# # 문자열 공백 제거
# data_str = '   홍  길동   '
# data_str = data_str.lstrip(' ')
# print(f'{data_str} : {len(data_str)}')

# data_str = '___홍  길동______'
# data_str = data_str.rstrip('_')
# print(f'{data_str} : {len(data_str)}')

# data_str = ' 0? 홍  길동 _$# '
# data_str = data_str.strip(' 0?_$#')
# print(f'{data_str} : {len(data_str)}')

# # 문자열 교체
# data_str = '10....20....30....40....50'
# data_str = data_str.replace('.'*4, '\t')
# print(data_str)

# # 문자열 자르기 
# data_str = '10, 20, 30, 40, 50'
# data_list = data_str.split(', ')
# for val in data_list :
#     print(val)

# # 문자열 구성확인
# data_str = '10, 20, 3o, 40, 50'
# data_list = data_str.split(', ')
# for val in data_list :
#     print(val, end=" ")
#     if not val.isdigit():
#         print("<=", end="")
#     print()

# # 문자열 "ABCDEFG"이 있을 때, 두번째 글자에서 네번째 글자까지 출력해주세요.
# ex_str = "ABCDEFG"
# print(ex_str[1:4])

# # 문자열 "AbcCDeEFggG"이 있을 때, 이 문자열을 모두 대문자로 바꾼 결과와 소문자로 바꾼 결과를 각각 출력해주세요.
# ex_str2 = "AbcCDeEFggG"
# print(ex_str2.upper())
# print(ex_str2.lower())

# # 문자열 "aaaAAbbBBcCCdE" 가 있다.
# # 1부터 위의 문자열의 길이까지의 수를 모두 더한 결과를 출력하여라.
# ex_str3 = "aaaAAbbBBcCCdE"
# total = 0
# for i in range(1, len(ex_str3)+1) :
#     total += i
# print(total)

# 실습
data_str = '파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다.'

find_str = input('찾을 문자열을 입력하세요 : ')
mask_str = input('마스킹할 문자열을 입력하세요 : ')
idx = -1
count = 1

while True :
    idx = data_str.find(find_str, idx + 1)
    if idx != -1 :
        print(f'[{idx}] ~ [{idx + len(find_str) -1}]')
        new_str = data_str.replace(find_str, mask_str, count)
        print(new_str)
        count += 1
    else :
        break
