import requests
from bs4 import BeautifulSoup


keywords = ['python', 'API', 'SQL']

def get_jobs(keyword):
  print(f"🔖 {keyword} Job List\n")
  url = f"https://remoteok.com/remote-{keyword}-jobs"
  response = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
  })
  soup = BeautifulSoup(response.content, 'html.parser')
  
  jobs = soup.find('table', id='jobsboard').find_all('tr', class_ = 'job')
  
  for job in jobs:
    title = job.find('h2', itemprop = 'title').text.strip()
    company = job.find('h3', itemprop = 'name').text.strip()
    location = job.find('div', class_ = 'location').text
    if location.startswith('💰'):
      location = 'No information'
    salary = job.find_all('div', class_ = 'location')[-1].text
    url = f"https://remoteok.com{job.find('a', itemprop = 'url')['href']}"
    print(f"Title: {title}\nCompany: {company}\nLocation: {location}\nSalary: {salary}\nUrl: {url}\n")


jobs_python = get_jobs(keywords[0])