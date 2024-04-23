# simple_crawler.py
import requests
from bs4 import BeautifulSoup

def simple_crawler(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.get_text())

if __name__ == "__main__":
    target_url = 'https://dictionary.cambridge.org/dictionary/english/milestone'
    simple_crawler(target_url)
