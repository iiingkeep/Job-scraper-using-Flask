'''
🧑‍💻 Dynamic Website Scrapeing 🧑‍💻
playwright로 브라우저를 열고 스크래핑을 진행할 페이지로 이동
BeautifulSoup를 이용하여 웹 스크래핑

playwright 진행 과정
1. 크롬 브라우저를 열어 wanted 웹사이트로 이동
2. 검색 버튼을 눌러 검색 페이지로 이동
3. 검색 input을 찾아 flutter 입력, 엔터
4. 포지션 탭 선택
5. 스크롤 다운 4번
'''

from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

# 브라우저 초기화. 크롬 사용
browser = p.chromium.launch(headless = False)
# 브라우저 새 탭을 열어 구글 페이지로 이동
page = browser.new_page()
page.goto('https://www.wanted.co.kr/')
time.sleep(3)

page.click('button.Aside_searchButton__rajGo')
time.sleep(3)

page.get_by_placeholder('검색어를 입력해 주세요.').fill('flutter')
time.sleep(3)

page.keyboard.down('Enter')
time.sleep(5)

page.click('a#search_tab_position')
time.sleep(5)

for x in range(5):
  page.keyboard.down('End')
  time.sleep(3)

content = page.content()

soup = BeautifulSoup(content, 'html.parser')
jobs = soup.find_all('div', class_ = 'JobCard_container__REty8')

jobs_db = []

for job in jobs:
  link = f"https://www.wanted.co.kr{job.find('a')['href']}"
  title = job.find('strong', class_ = 'JobCard_title__HBpZf').text
  company_name = job.find('span', class_ = 'JobCard_companyName__N1YrF').text
  reward = job.find('span', class_ = 'JobCard_reward__cNlG5').text

  job = {
    'title': title,
    'company_name': company_name,
    'reward': reward,
    'link': link,
  }
  jobs_db.append(job)

print(jobs_db)
print(len(jobs_db))

p.stop()