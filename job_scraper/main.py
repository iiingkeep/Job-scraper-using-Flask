from flask import Flask, render_template, request, redirect, send_file
from static_website import get_jobs
from file import save_to_file

app = Flask('JobScraper')

db = {}

# @: decorator. 특정 주소의 route를 지정해주는 역할을 한다. 바로 밑줄에 함수를 입력 시 그 주소에 갔을 때 함수를 호출하며 응답. 
@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/search')
def search():
  keyword = request.args.get('keyword')
  if keyword == None:
    return redirect('/')
  if keyword in db:
    jobs = db[keyword]
  else:
    jobs = get_jobs(keyword)
    db[keyword] = jobs
  return render_template('search.html', keyword=keyword, jobs=jobs)

@app.route('/export')
def export():
  keyword = request.args.get('keyword')
  if keyword == None:
    return redirect('/')
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)

# 서버와의 연결 요청.
app.run('0.0.0.0',  debug=True)