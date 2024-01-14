import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {"Title": []}
for p in range(2846, 3048, 1):
    url = "https://www.ptt.cc/bbs/Japandrama/index" + str(p) + ".html"
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'lxml')
    titles = sp.find_all("div", class_="title")

    for title in titles:
        title_link = title.find("a")
        if title_link:
            title_text = title_link.text.split("]")
            # 添加檢查以確保列表長度足夠
            if len(title_text) > 1:
                data["Title"].append(title_text[1])
            else:
                data["Title"].append("")

# 创建DataFrame
df = pd.DataFrame(data)

# 将DataFrame保存为CSV文件
df.to_csv("japandrama_titles.csv", index=False)

