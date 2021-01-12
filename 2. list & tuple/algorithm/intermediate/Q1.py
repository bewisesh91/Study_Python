# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

# test_case = 3

# case_1 
# N = 5
# Data = 477162 658880 751280 927930 297191

# case_2
# N = 5
# Data = 565469 851600 460874 148692 111090

# case_3
# N = 10
# Data = 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

test_case = int(input())
for i in range(test_case) :
    N = int(input())
    Data = list(map(int,input().split(' ')))
    result = max(Data) - min(Data)
    print(f'#{i+1} {result}')