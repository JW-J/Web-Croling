import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}&vjk=f6294b6c85e1cb47'


def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')

    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_pages = pages[-1]
    return max_pages

# TEST2.py 에서 5를 반환받아 last_page(5)가 대입된다.
# 그렇기 때문에 1~5까지 * 50을 해준값을 반환한다.
def extract_indeed_jobs(last_page):
    for page in range(last_page):
        print(f"&start={page*LIMIT}")


