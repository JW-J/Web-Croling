from WebScrapping_uses1 import extract_indeed_pages, extract_indeed_jobs

# TEST.py 파일에서 총 페이지의 수(5) 를 가져와서 last_indeed_page(5)를 넣는다.
last_indeed_page = extract_indeed_pages()

# last_indeed_page(5)를 TEST.py 의 extract_indeed_jobs에 5를 넣어준다.
extract_indeed_jobs(last_indeed_page)
# 결과값
# &start=0
# &start=50
# &start=100
# &start=150
# &start=200