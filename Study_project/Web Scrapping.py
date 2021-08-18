import requests
from bs4 import BeautifulSoup

# 해당 페이지의 html 을 모두 가져옴.
indeed_result = requests.get('https://www.indeed.com/jobs?q=python&limit=50&vjk=f6294b6c85e1cb47')
#print(indeed_result.text)

# html 을 indeed_soup test로 저장
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

# html의 텍스트에서 div 태그의 클래스명:pagination 을 찾아서 넣는다.
# 페이지가 몇개인지 알기 위해서.
pagination = indeed_soup.find("div", {"class": "pagination"})

# 태그(div)의 클래스(pagination)을 찾아서 넣은 pagination_list에서 pages에 a태그만 추출해서 넣는다.
links = pagination.find_all('a')

# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# print(pages)

# pages안에 있는 a태그 리스트에서 span 태그만 가져와서 page에넣고 이를 spans 배열에 삽입한다.
# 예제0) String 으로 가져오기.
pages = []
for link in links:
    pages.append(link.string)
pages = pages[0:-1]
#print(pages)
# 예제0) 결과 값
# ['2', '3', '4', '5'] / 문자열(string)

# 예제1) 태그 가져오기.
# spans 배열에 삽입.
spans = []
for link in links:
    spans.append(link.find("span"))
#print(spans[0:-1])
#  예제1) 결과 값
# [<span class="pn">2</span>, <span class="pn">3</span>, <span class="pn">4</span>, <span class="pn">5</span>]

# 예제2) 문자열 가져오기
# links 내 배열에 들어가는 끝에 문자열(next) 포함되어있어서 에러발생함.
pages = []
for link in links[:-1]:
    pages.append(int(link.string))
print(pages)
# 예제2) 결과 값
# [2, 3, 4, 5]  / integer(정수형)


