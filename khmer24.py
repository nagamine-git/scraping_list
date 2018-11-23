from tqdm import tqdm
from bs4 import BeautifulSoup
import requests
import re

# 対象のURL入力
print("スクレイピングしたいURLを入力して下さい")
url = str(input(">>> "))
result = ''

# urlからsoup(lxml形式のページ内容)を返すメソッド
def url_to_soup(url):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = user_agent)
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
res_ary = []

for i in tqdm(range(0, 9)):
    soup = url_to_soup("https://www.khmer24.com/en/cars-and-vehicles-in-kandal.html?category=cars-and-vehicles&sortby=latestads&per_page="+str(i*50))
    for a in soup.find_all("a", class_="post"):
        res_ary.append(a.get('href'))

for child in tqdm(res_ary):
    soup = url_to_soup(child)
    res += (soup.find("p", class_="name").text + "," + soup.find("a", class_="header").get("href") + "\n")

write_csv(res)