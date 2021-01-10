# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로 구분하는 프로그램을 작성하십시오.

url = 'http://www.example.com/test?p=1&q=2'
new_url = url.split('/')
print(f'protocol: {new_url[0][:-1]}')
print(f'host: {new_url[2]}')
print(f'others: {new_url[3]}')
