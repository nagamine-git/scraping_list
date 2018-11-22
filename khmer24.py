from tqdm import tqdm
from bs4 import BeautifulSoup
import urllib.request
import re

# 対象のURL入力
print("スクレイピングしたいURLを入力して下さい")
url = str(input(">>> "))
result = ''

# urlからsoup(lxml形式のページ内容)を返すメソッド
def url_to_soup(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    return soup

def write_csv (result) :
    file_name = "./result.csv"
    try:
        file = open(file_name, 'w', encoding='utf-16')
        file.write(str(result))
    except Exception as e:
        print(e)
    finally:
        file.close()
