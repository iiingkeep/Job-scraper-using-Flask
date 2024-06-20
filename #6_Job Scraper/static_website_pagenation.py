'''
🧑‍💻 Static Website Scraping 🧑‍💻
url = https://weworkremotely.com/remote-full-time-jobs#job-listings
목표 = 구인 사이트인 weworkremotely의 full-time 카테고리에 올라온 모든 구인글에서 회사명, 직무명, full-time 여부, 근무지, url 추출

scraping 할 부분
1. section 태그 안의 모든 li
2. li 중 필요 없는 데이터를 담고 있는 첫번째와 마지막 li 제외
3. li 태그 안의 a 태그 안의 span 태그들 중 회사 이름, 직무명, Full-time 여부, 근무지 추출
4. 페이지 개수를 구해 모든 페이지에서 실행

<section class="jobs">...</section>
<li class="feature">...</li>
<a href="/remote-jobs/playfly-need-senior-blockchain-engineer-smart-contract-web3-experts">...</a>
<span class="company">Playfly</span><br>
<span class="title">Need Senior Blockchain Engineer - Smart contract &amp; Web3 Experts</span>
<span class="featured">featured</span><br>
<span class="company">Full-Time</span>
<span>/</span>
<span class="region company">Anywhere in the World</span>
'''


import requests
from bs4 import BeautifulSoup

all_jobs = []

# 해당 페이지에서 회사명, 직무, Full-time 여부, 근무지를 추출해 job_data라는 딕셔너리를 생성하고, 각각의 딕셔너리를 all-jobs 리스트에 넣는 함수
def scrape_page(url):
  print(f"Scraping {url} \n")
  response = requests.get(url)

  # response.content: 그 url의 html resource가 나온다.
  # BeautifulSoup: HTML/XML resource를 파싱해주는 라이브러리. 
  # soup = BeautifulSoup(resource, option)
  soup = BeautifulSoup(response.content, 'html.parser')

  # 1+2. section태그 안에서 첫번째와 마지막을 제외한 모든 li 가져오기
  jobs = soup.find('section', class_ = 'jobs').find_all('li')[1:-1]
  # class는 예약어이기 때문에 class_로 사용해야한다.

  # 3. li 태그 안에 있는 span 태그에서 classname을 통해 직무, 회사명, 포지션, 지역 데이터 추출
  for job in jobs:
    title = job.find('span', class_= 'title').text
    try:
      url = job.find('div', class_ = 'tooltip--flag-logo').next_sibling['href']
    except KeyError:
      url = 'You need log-in'
    company, position, region = job.find_all('span',   class_ = 'company')[0:3]
    job_data = {
      "title": title,
      "company": company.text,
      "position": position.text,
      "region": region.text,
      "url": f"https://weworkremotely.com{url}"
    }
    all_jobs.append(job_data)
  print(f"Number of tasks done: {len(all_jobs)} \n")

# 페이지의 갯수를 구하는 함수
def get_pages(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  return len(soup.find('div', class_ = 'pagination').find_all('span', class_ = 'page'))
  

total_pages = get_pages('https://weworkremotely.com/remote-full-time-jobs?page=1')

# 모든 페이지 scraping
for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
  scrape_page(url)

print(f"Total number of posts: {len(all_jobs)}")