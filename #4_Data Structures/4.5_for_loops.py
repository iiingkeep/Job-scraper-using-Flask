# For Loop: 리스트 또는 튜플에서 안에 있는 데이터들에 차례대로 접근 가능
# for variable in variabels: 형태로 일반적으로 사용

websites = (
  'google.com',
  'airbnb.com',
  'https://twitter.com',
  'facebook.com',
  'https://tiktok.com'
)

# websites 튜플의 데이터에 차례로 접근해 아래의 구문 출력
for website in websites:
  print('website is equals to', website)
'''
website is equals to google.com
website is equals to airbnb.com
website is equals to https://twitter.com
website is equals to facebook.com
website is equals to https://tiktok.com
'''