# ✨Code Challenge!✨
# 다음 목록의 웹사이트에 대해 웹사이트가 응답하는 HTTP Status Code에 따라 상태 문구 출력하기
# HTTP코드를 생성해주는 사이트 https://httpstat.us/xxx 이용
websites = [
  "google.com",
  "https://httpstat.us/502",
  "https://httpstat.us/404",
  "https://httpstat.us/300",
  "https://httpstat.us/200",
  "https://httpstat.us/101"
]

from requests import get

results = {}

for website in websites:
  if not website.startswith('https://'):
    website = f"https://{website}"
  response = get(website)
  if response.status_code < 200:
    results[website] = "INFORMATION"
  elif response.status_code < 300:
    results[website] = "SUCCESSFUL"
  elif response.status_code < 400:
    results[website] = "REDIRECTION"
  elif response.status_code < 500:
    results[website] = "CLIENT ERROR"
  else:
    results[website] = "SERVER ERROR"

print(results)

'''
{
'https://google.com': 'SUCCESSFUL',
'https://httpstat.us/502': 'SERVER ERROR',
'https://httpstat.us/404': 'CLIENT ERROR',
'https://httpstat.us/300': 'REDIRECTION',
'https://httpstat.us/200': 'SUCCESSFUL',
'https://httpstat.us/101': 'INFORMATION'
}
'''