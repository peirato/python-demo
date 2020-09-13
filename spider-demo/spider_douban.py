import requests
from bs4 import BeautifulSoup

user_agent = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}


def main(page):
    url = 'https://movie.douban.com/top250?start=' + str((page -1) * 25) + '&filter='
    html_doc = request_douban(url)
    soup = BeautifulSoup(html_doc, 'lxml')
    list = soup.find(class_='grid_view').find_all('li')

    for item in list:
        print (item.find(class_='title').string)
        print (item.find(class_='rating_num').string)
        print(item.find(class_='inq').string)


def request_douban(url):
    response = requests.get(url, headers=user_agent)
    try:
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        print("error")
        return None


if __name__ == '__main__':
    main(1)
