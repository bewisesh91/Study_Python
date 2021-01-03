# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 리스트 객체가 주어졌을 때 짝수만 항목으로 가지는 리스트 객체를 생성하는 코드를 작성하십시오.

num_list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]

even_num = [x for x in num_list if x % 2 == 0]
print(even_num)