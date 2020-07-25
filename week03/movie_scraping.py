import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://m.stock.naver.com/',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

sports = soup.select('#old_content > table > tbody > tr')

for stock in stocks:
    a_tag = stock.select_one('td.title > div > a')
    if a_tag is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt'] # img 태그의 alt 속성값을 가져오기
        stock_item = a_tag.text
        price = stock.select_one('td.point').text# a 태그 사이의 텍스트를 가져오기
        print(rank,stock_item,price)