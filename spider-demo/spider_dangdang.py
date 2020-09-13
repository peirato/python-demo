import urllib.request
import re
import requests
from bs4 import BeautifulSoup

# if __name__ == '__main__':
#     url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1';

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))
#
# content = 'Xiaoshuaib has 100 bananas'
# res = re.match('^Xi.*(\d+)\s.*s$', content)
# print(res.group(1))
#
# content = 'Xiaoshuaib has 100 bananas'
# res = re.match('^Xi.*?(\d+)\s.*s$', content)
# print(res.group(1))

html_doc = """

<html><head><title>学习python的正确姿势</title></head>
<body>
<p class="title"><b>小帅b的故事</b></p>

<p class="story">有一天，小帅b想给大家讲两个笑话
<a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
<a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
他问大家，想听长的还是短的？</p>

<p class="story">...</p>

"""


def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def beautiful_soup():
    soup = BeautifulSoup(html_doc, 'lxml')
    print(soup.title.string)
    print(soup.p.string)
    print(soup.title.parent.name)
    print(soup.a)
    print(soup.find_all('a'))
    print(soup.find(id="link2"))
    print(soup.get_text())

    print(soup.select("title"))
    print(soup.select("body a"))
    print(soup.select("p > #link1"))


if __name__ == '__main__':
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1';
    print(request_dandan(url))

    beautiful_soup()
