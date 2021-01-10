# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 회문 여부를 판단하는 코드를 작성하십시오.

def palindrome(word) :
    for i in range(len(word)) :
        if word[i] != word[-(i+1)] :
            return False
    return True

user_input = input()
if palindrome(user_input) :
    print('입력ㄷ하신 단어는 회문(Palindrome)입니다.')