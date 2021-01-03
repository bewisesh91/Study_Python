# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.

def fibo(x) :
    if x == 1 or x == 2 :
        return 1
    return fibo(x-1) + fibo(x-2)

result = [fibo(x) for x in range(1, 11)]
print(result)