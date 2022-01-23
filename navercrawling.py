# Ch.2-16 응용 해보기
# 급상승 검색어만 검색해주는 naver datalab 페이지 사용
from bs4 import BeautifulSoup
import requests
from datetime import datetime

# 네이버는 크롤링 로봇 막음. 우리는 로봇아니라고 알려주기
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://www.nate.com/main/srv/news/data/keywordList.today.json?v=202104300430"

 #? 이전: 공통 / 이후: 파라미터(서버를 만들 때 재료로 사용)
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1
# 네이버 실시간검색어의 공통점 : span 태그- item_title 클래스
results = soup.findAll('keyword_name')

search_rank_file = open("rankresult.txt", "a", encoding="UTF-8")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank, "위 : ", result.get_text(), "\n")
    rank += 1