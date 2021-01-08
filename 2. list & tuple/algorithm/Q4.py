# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 다음의 결과와 같이 구구단 2단부터 9단의 결과값 중에 3의 배수거나 7의 배수인 수를 제외한 값을 리스트 객체 result 안에 각 단마다 리스트를 만들어 삽입하고 이를 출력하십시오.
# 결과 : [[2, 4, 8, 10, 16], [], [4, 8, 16, 20, 32], [5, 10, 20, 25, 40], [], [], [8, 16, 32, 40, 64], []]

gugudan = []

for i in range(2, 10) :
    dan = []
    for j in range(1, 10) :
        dan.append(i*j)
    dan_n3 = [x for x in dan if x % 3 != 0]
    new_dan = [y for y in dan_n3 if y % 7 != 0]
    gugudan.append(new_dan)

print(gugudan)