# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 기존의 맥주 가격을 5% 인상하려고 할 경우 딕셔너리 내포 기능을 이용한 코드를 작성하십시오.

beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}

new_price = {key: value*(1.05) for key, value in beer.items()}
print(beer)
print(new_price)
