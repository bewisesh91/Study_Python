# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 항목 값으로는 0을 갖는 2*3*4 형태의 3차원 배열을 생성하는 리스트 내포 기능을 이용한 프로그램을 작성하십시오.

a = [0 for i in range(4)]
b = [a for i in range(3)]
c = [b for i in range(2)]
print(c)