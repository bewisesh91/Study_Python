# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.

# 단어를 분리하고, 리스트로 만들어서 뒤에서 부터 출력한다

words = 'A better tomorrow'
new_list = words.split(' ')
new_words = ""
for i in range(len(new_list)) :
    new_words = new_words + new_list[-(i+1)] + ' '

print(new_words)

# new_list.reverse()
# print(' '.join(new_list))