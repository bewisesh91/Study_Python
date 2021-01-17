# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 사용자가 입력한 문장에서 공백을 이용해 단어들을 구분하고, 중복된 단어없이 단어를 콤마(,)로 구분해 사전순으로 출력하는 프로그램을 작성하십시오.

user_input = '산 하늘 강 바다 하늘 강 들'
result = sorted(set(user_input.split(' ')))
print(','.join(result))