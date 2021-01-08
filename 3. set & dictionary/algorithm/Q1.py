# _*_ coding : utf-8 _*_

# 딕셔너리 객체를 활용하여 총점과 평균 구하기
# 학생 정보(학생의 수, 국어/영어/수학 점수)를 입력 받아 총점과 평균을 계산


count = int(input('총 학생의 수를 입럭하세요 : '))

scores = []

for i in range(1, count + 1) :
    score = {}
    score['name'] = input('학생의 이름을 입력하세요 : ')
    score['kor'] = int(input(f'{score["name"]} 학생의 국어 점수를 입력하세요. : '))
    score['mat'] = int(input(f'{score["name"]} 학생의 수학 점수를 입력하세요. : '))
    score['eng'] = int(input(f'{score["name"]} 학생의 영어 점수를 입력하세요. : '))
    scores.append(score)

for score in scores :
    total = 0
    for key in score :
        if key != 'name' :
            total += score[key]
    print(f'{score["name"]} => 총점 : {total}, 평균 : {total/3:0.2f}')

kor_total, mat_total, eng_total = 0, 0 ,0
for score in scores :
    for key in score :
        if key == 'kor' :
            kor_total += score[key]
        elif key == 'mat' :
            mat_total += score[key]
        elif key == 'eng' :
            eng_total += score[key]
print(f'국어 => 총점 : {kor_total}, 평균 : {kor_total/len(scores):0.2f}')
print(f'수학 => 총점 : {mat_total}, 평균 : {mat_total/len(scores):0.2f}')
print(f'영어 => 총점 : {eng_total}, 평균 : {eng_total/len(scores):0.2f}')