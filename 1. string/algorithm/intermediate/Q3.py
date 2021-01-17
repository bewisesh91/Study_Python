# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
# 예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.

test_case = int(input())

for i in range(test_case) :
    str1 = input()
    str2 = input()
    max_count = 0
    for j in str1 :
        count = str2.count(j)    
        if count > max_count :
            max_count = count
    
    print(f'#{i+1} {max_count}')
