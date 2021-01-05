# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 콤마(,)로 구분해 숫자를 입력하고, 입력된 숫자 중 홀수를 콤마(,)로 구분해 출력하는 리스트 내포 기능을 이용한 프로그램을 작성하십시오.

user_input = list(input().split(","))
user_list = ",".join([i for i in user_input if int(i) % 2 != 0])
print(user_list)