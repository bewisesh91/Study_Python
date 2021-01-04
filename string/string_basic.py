# 문자열 "ABCDEFG"이 있을 때, 두번째 글자에서 네번째 글자까지 출력해주세요.
ex_str = "ABCDEFG"
print(ex_str[1:4])

# 문자열 "AbcCDeEFggG"이 있을 때, 이 문자열을 모두 대문자로 바꾼 결과와 소문자로 바꾼 결과를 각각 출력해주세요.
ex_str2 = "AbcCDeEFggG"
print(ex_str2.upper())
print(ex_str2.lower())

# 문자열 "aaaAAbbBBcCCdE" 가 있다.
# 1부터 위의 문자열의 길이까지의 수를 모두 더한 결과를 출력하여라.
ex_str3 = "aaaAAbbBBcCCdE"
total = 0
for i in range(1, len(ex_str3)+1) :
    total += i
print(total)

