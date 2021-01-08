# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

user_input = input()
uc, lc = 0, 0
for x in user_input:
    if x.isupper() :
        uc += 1
    elif x.islower():
        lc += 1
print(f'UPPER CASE {uc}')
print(f'LOWER CASE {lc}')