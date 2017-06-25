import requests
url = "http://item.jd.com/2967929.html"

def getHTMLText():
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[:1000])

    except:
        print("爬取失败")


if __name__ == "_main_":
    getHTMLText()