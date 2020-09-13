import json

import requests
from bs4 import BeautifulSoup

user_agent = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}


def main(page):
    url = 'https://movie.douban.com/top250?start=' + str((page - 1) * 25) + '&filter='
    html_doc = request_douban(url)
    soup = BeautifulSoup(html_doc, 'lxml')
    list = soup.find(class_='grid_view').find_all('li')

    data_list = []

    for item in list:
        title = item.find(class_='title').string
        print(title)
        rating_num = item.find(class_='rating_num').string
        print(rating_num)
        inq = item.find(class_='inq').string
        print(inq)

        data = {'title': title, 'rating_num': rating_num, 'inq': inq}

        data_list.append(data)

    return data_list


def request_douban(url):
    response = requests.get(url, headers=user_agent)
    try:
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        print("error")
        return None


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')


if __name__ == '__main__':
    data_list = main(1)
    write_to_file(json.dumps(data_list))
