# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

test_case = int(input())

for i in range(test_case) :
    str1 = input()
    str2 = input()
    if str1 in str2 :
        print(f'#{i+1} 1')
    else :
        print(f'#{i+1} 0')