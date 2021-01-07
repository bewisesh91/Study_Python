# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리 객체를 생성하는 코드를 작성해봅시다.
# 이 때 딕셔너리 내포 기능을 사용하며, 원소의 공백은 제거합니다.

fruit = ['   apple    ','banana','  melon']
new_dict = {x.strip(): len(x.strip()) for x in fruit}

print(new_dict)