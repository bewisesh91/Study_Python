# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 아래의 상품 딕셔너리 데이터를 가격에 따라 내림차순으로 정렬하는 프로그램을 작성하십시오.
# "TV": 2000000,
# "냉장고": 1500000,
# "책상": 350000,
# "노트북": 1200000,
# "가스레인지": 200000,
# "세탁기": 1000000,

products = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000,
}

# new_product = {value : key for key, value in products.items()}

# products_list = []
# for key, value in new_product.items() :
#     products_list.append(key)

# products_list = sorted(products_list, reverse=True)

# for price in products_list :
#     print(f'{new_product[price]}: {products[new_product[price]]}')

products = sorted(products.items(), reverse=True, key = lambda item: item[1])
for key, value in products :
    print(f'{key}: {value}')

