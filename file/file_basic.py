# 파일 열기
# 파일 객체 = open( 파일 이름, 파일 열기 모드 )
# 파일 이름에는 파일의 주소를 넣어 줘야 함
# 파일 열기 모드에는 다음과 같은 것들이 있음
# r : 파일을 읽기 위해서 연다.(기본값)
# w : 파일에 데이터를 쓰기 위해서 연다. 이때, 기존 내용은 모두 사라지고 새로 무언가를 쓸 준비를 한다.
# x : 새로운 파일을 생성해야 한다. 이때, 같은 이름의 파일이 존재하면 error가 발생한다.
# a : 파일의 뒷부분에 데이터를 추가하기 위해 파일을 연다.
# b : 파일을 바이너리 데이터로 본다.
# t : 파일을 텍스트 데이터로 본다.( 줄바꿈, 인코딩 등을 자동으로 처리 )
# a : 기존 파일 업데이트를 위해서 파일을 연다.

# 파일 닫기
# 파일 객체.close()

# f = open( "a.txt", "w" )
# f.write( "안녕하세요 \n")
# f.close()

	
# f = open( "a.txt", "w" )
# f.write( "반가워요 \n")
# f.close()
# f = open( "a.txt", "r" )
# print( f.read() )

# 실습 # 1
f = open( "/Users/kakao/Desktop/python_practice/Study_Python/file/a.txt", "w" )
f.write( "반갑습니다\n안녕히계세요")
f.close()
f = open( "/Users/kakao/Desktop/python_practice/Study_Python/file/a.txt", "r" )
print( f.read() )

# 실습 # 2
f = open( "/Users/kakao/Desktop/python_practice/Study_Python/file/b.txt", "r" )
user_info = f.readlines()
print(user_info)

id = input('아이디를 입력해주세요 : ')
pw = input('비밀번호를 입력해주세요 : ')

check = False
for i in range(len(user_info)) :
    check_info = user_info[i].split()
    if check_info[0] == id and check_info[1] == pw :
        check = True
        break
    else :
        check = False

if check :
    print('로그인 성공')
else :
    print('로그인 실패')



# 실습 # 3
# name.txt 라는 파일을 읽어와 그 내용을 출력해주세요.
# name.txt라는 파일이 없다면 "파일이 없습니다." 라는 메세지를 출력해주세요.

try : 
    f = open( "/Users/kakao/Desktop/python_practice/Study_Python/file/name.txt", "r" )
    info = f.readlines()
    print(info)
    f.close()
except FileNotFoundError :
    print('파일이 없습니다.')
