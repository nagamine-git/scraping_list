from tqdm import tqdm
from bs4 import BeautifulSoup
import requests
import re

# 対象のURL入力
print("スクレイピングしたいURLを入力して下さい")
url = str(input(">>> "))
result = ''

# urlからsoup(lxml形式のページ内容)を返すメソッド
def url_to_soup(url, page_num):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get("https://www.khmer24.com/en/cars-and-vehicles-in-phnom-penh.html?category=cars-and-vehicles&sortby=latestads&per_page="+str(page_num), headers = user_agent)
    soup = BeautifulSoup(response.text, "lxml")
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

res = ""

for i in range(1, 300):
    soup = url_to_soup(url, i*50)

    for a in soup.find_all("a", class_="username-tag"):
        res += (a.text + "," +a.get('href') + "\n")

write_csv(res)