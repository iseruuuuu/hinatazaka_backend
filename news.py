import requests
from bs4 import BeautifulSoup

url = 'https://www.hinatazaka46.com/s/official/artist/2?ima=0000'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

news_section = soup.find('section', class_='p-news-top__list')


if news_section:
    latest_news = news_section.find('li', class_='p-news-top__list__item')
    
    if latest_news:
        title = latest_news.find('p', class_='p-news-top__list__item__title').text.strip()
        date = latest_news.find('time', class_='p-news-top__list__item__date').text.strip()
        news_url = latest_news.find('a', class_='p-news-top__list__item__link')['href']

        print(f'タイトル: {title}')
        print(f'日付: {date}')
        print(f'URL: {news_url}')
    else:
        print("最新ニュースが見つかりませんでした。")
else:
    print("ニュースセクションが見つかりませんでした。")
