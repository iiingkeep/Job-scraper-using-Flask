# Mini project <Is Website Down or Not?>
# 목록에 있는 웹사이트가 다운되었는지 판별하는 프로그램 만들기

# 1단계. websites url formatting
# websites 튜플의 데이터에 대해 'https://' 로 시작하는지 확인 후 'https://'로 시작하지 않는 데이터들은 데이터 앞에 'https://' string을 붙여 'https://'로 시작하는 url 만들기
websites = (
  'google.com',
  'airbnb.com',
  'https://twitter.com',
  'facebook.com',
  'https://tiktok.com'
)

# websites 튜플의 데이터에 차례로 접근해 https:// 로 시작하는지 확인, false라면 수정해야 한다는 정보를 출력
for website in websites:
  if website.startswith('https://'):
    print('Good to go')
  else:
    print('We have to fix it')
'''
We have to fix it
We have to fix it
Good to go
We have to fix it
Good to go
'''

# https://로 시작하지 않는 경우만 다룰 경우, if구문에서 True를 반환할 경우는 고려하지 않아도 된다.
# if not ~ 구문을 사용해 코드를 간결하게 만든다.
for website in websites:
  if not website.startswith('https://'):
    print('have to fix')

# https://로 시작하지 않는 각각의 website 데이터들에 한해, 데이터 앞에 'https://' string을 추가해준다.
for website in websites:
  if not website.startswith('https://'):
    website = f"https://{website}"
  print(website)
'''
https://google.com
https://airbnb.com
https://twitter.com
https://facebook.com
https://tiktok.com
'''



# 2단계. 웹사이트에 get 요청을 해 status code를 받기
# requests 모듈 설치 후 get function을 import.
# get function은 return값으로 response를 받는다. 응답으로 받은 정보 중 우리가 필요한 정보는 status code.
from requests import get

for website in websites:
  if not website.startswith('https://'):
    website = f"https://{website}"
  response = get(website)
  print(response, response.status_code)
'''
<Response [200] 200>
<Response [200] 200>
<Response [200] 200>
<Response [200] 200>
<Response [200] 200>
'''
# 각각의 website의 상태코드가 200이라면 ok, 아니면 not ok 출력
for website in websites:
  if not website.startswith('https://'):
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    print(f"{website} is OK")
  else:
    print(f"{website} is not OK")
'''
https://google.com is OK
https://airbnb.com is OK
https://twitter.com is OK
https://facebook.com is OK
https://tiktok.com is OK
'''

# 3단계. status code에 따라 웹사이트의 상태 데이터를 딕셔너리에 보기 좋게 정리 
# results라는 dictionary를 생성 후, 검사한 사이트에 따른 결과 데이터 집어넣기
results = {}
for website in websites:
  if not website.startswith('https://'):
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    results[website] = "OK"
  else:
    results[website] = "FAILED"
print(results)
'''
{
'https://google.com': 'OK',
'https://airbnb.com': 'OK',
'https://twitter.com': 'OK',
'https://facebook.com': 'OK',
'https://tiktok.com': 'OK'
}
'''