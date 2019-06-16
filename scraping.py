# coding:utf-8
import urllib3
from bs4 import BeautifulSoup
import certifi

# 千と千尋のセリフをスクレイピングしてくるプログラム

# アクセスするURL
url = "https://lolipop-teru.ssl-lolipop.jp/ghibli/senchi.html"

# httpsの証明書検証を実行している
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())
r = http.request('GET', url)

soup = BeautifulSoup(r.data, 'html.parser')

# セリフの抽出
serif = soup.findAll("p")
serif = [i.text.strip("\n") for i in serif]
serif.pop(0)
serif.pop(0)

while "" in serif:
    serif.remove("")

# name_listの作成
name = []
name_list = []
a = 0
j = 0
for i in serif:
    # サイトのhtml読んでうまくいくように条件分岐でセッティング
    if i[0] == "\t":
        if '"' not in i:
            i = i.replace("\t", str(name) + ": ")
    elif "\t" in i:
        if ":" not in i:
            i = i.replace("\t", ": ")
    # serifをキャラ名とテキストに分割
    if '"' not in i:
        ser = i.split("\t")
        ser = i.split(":")
    else:
        i = i.lstrip('"')
        ser = i.rstrip('"')

    # txtファイルへの書き出し
    if len(ser) == 2:
        if ser[0] not in name_list:
            name_list.append(ser[0])
            new = open(ser[0] + ".txt", "w+")
            new.close()
        serif[j] = [ser[0], ser[1]]
        f = open(ser[0] + ".txt", "a+")
        f.write(ser[1] + "\n")
        f.close()
        name = ser[0]
    elif len(ser) == 1:
        if a == 0:
            name_list.append("Narration")
            new = open("Narration.txt", "w+")
            new.close()
            a = 1
        f = open("Narration.txt", "a+")
        f.write(ser + "\n")
        f.close()
        serif[j] = ["Narration", ser]
        name = "Narration"
    j = j + 1

# name一覧表示
print(name_list)
