# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.

string = 'abcdefgabc'

new_dict = {}
for i in string :
    try :
        if new_dict[i]:
            new_dict[i] += 1
    except :
        new_dict[i] = 1
for key, values in new_dict.items() :
    print(f'{key},{values}')

