# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.

num_list = [int(input()) for i in range(5)]
print(f'입력된 값 {num_list}의 평균은 {sum(num_list)/len(num_list):0.1f}입니다.')