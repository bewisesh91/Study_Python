# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.


str_input = input()

letters = 0
digits = 0
for x in str_input :
    if x.isalpha() :
        letters += 1
    elif x.isdigit() :
        digits +=1

print(f'LETTERS {letters}')
print(f'DIGITS {digits}')