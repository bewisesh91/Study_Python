# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 리스트의 항목 중 중복이 되는 항목을 제거하는 함수를 정의하고 이 함수를 이용해 [12,24,35,24,88,120,155,88,120,155]에서 중복이 제거된 리스트를 출력하십시오.

def adj_list(a) :
    new_list = sorted(list(set(a)))
    return new_list

data = [12,24,35,24,88,120,155,88,120,155]
print(adj_list(data))