# 크기가 4인 리스트를 만들어주세요.
# for문을 통해 인덱스가 0인 리스트의 값부터 인덱스가 5인 리스트의 값까지 출력해주세요.
# 예외가 발생하면 "해당하는 인덱스가 없습니다." 메세지를 출력해주세요.

ex_list = [0]*4

for i in range(6) :
    try :
        print(ex_list[i])
    except IndexError :
        print("IndexError")


# name.txt 라는 파일을 읽어와 그 내용을 출력해주세요.
# name.txt라는 파일이 없다면 "파일이 없습니다." 라는 메세지를 출력해주세요.

try : 
    f = open( "/Users/kakao/Desktop/python_practice/Study_Python/file/name.txt", "r" )
    info = f.readlines()
    print(info)
    f.close()
except FileNotFoundError :
    print('파일이 없습니다.')
