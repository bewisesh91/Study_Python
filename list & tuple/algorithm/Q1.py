# _*_ coding : utf-8 _*_

# Q2.py

# 리스트 객체를 활용하여 총점과 평균 구하기
# 학생 정보(학생의 수, 국어/영어/수학 점수)를 입력 받아 총점과 평균을 계산

scores = []
count = int(input('총 학생수를 입력하세요 : '))

for i in range(1, count + 1) : 
    kor = int(input(f'학생{i}의 국어 점수를 입력하세요 : '))
    math = int(input(f'학생{i}의 수학 점수를 입력하세요 : '))
    eng = int(input(f'학생{i}의 영어 점수를 입력하세요 : '))
    score = [kor, math, eng]
    scores.append(score)

for i, score in enumerate(scores) :
    total = 0
    for s in score :
        total += s
    print(f'학생{i+1}의 총점 : {total}, 평균 : {total / len(score):0.2F}')