# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 한 학생의 시험 성적(1차, 2차) 점수를 튜플로 저장하고 이 튜플을 항목으로 갖는 리스트 객체가 있습니다.
# 이 때 첫 번째 학생은 (90, 80), 두 번째 학생은 (85, 75), 세 번째 학생은 (90, 100)의 점수를 갖습니다.
# 다음과 같이 결과를 만들기 위한 프로그램을 작성하십시오.
# 1번 학생의 총점은 170점이고, 평균은 85.0입니다.
# 2번 학생의 총점은 160점이고, 평균은 80.0입니다.
# 3번 학생의 총점은 190점이고, 평균은 95.0입니다.

# num_student = int(input('학생 수를 입력해주세요 : ' ))

# scores = []
# for i in range(num_student) :
#     test_1st = int(input('1차 성적을 입력하세요 : '))
#     test_2nd = int(input('2차 성적을 입력하세요 : '))
#     score = (test_1st, test_2nd)
#     scores.append(score)

# for i, score in enumerate(scores) :
#     total = 0
#     for s in score :
#         total += s
#     print(f'{i+1}번 학생의 총점은 {total}이고, 평균은 {total/len(score):0.1f}')


num_student = int(input('학생 수를 입력해주세요 : ' ))

scores = []
for i in range(num_student) :
    score = list(map(int, input().split(" ")))
    scores.append(score)

for i, score in enumerate(scores) :
    total = 0
    for s in score :
        total += s
    print(f'{i+1}번 학생의 총점은 {total}이고, 평균은 {total/len(score):0.1f}')