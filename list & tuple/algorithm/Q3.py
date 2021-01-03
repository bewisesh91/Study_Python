# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
# 문장 : 'Python is one of the most widely used programming languages, and it has been around for more than 28 years now. '

sentence = 'Python is one of the most widely used programming languages, and it has been around for more than 28 years now. '
answer = [char for char in sentence if char.lower() not in 'aeiou']
final_answer= ''.join(answer)
print(final_answer)