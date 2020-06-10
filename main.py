import requests
from bs4 import BeautifulSoup


def get_id(url):
    if 'https://' not in url:
        return url
    id_part = url.split('/')[-1]
    if '=' in id_part:
        id_part = id_part.split('v=')[-1]
    return id_part[:11]

def print_results(res):
    print()
    if res:
        print(res[2])
        print('•' * (len(res[2]) // 2))
        print(f'{res[1]}: {res[0]}')
    else:
        print("This video is not in the database yet, please try again later (this video is getting analyzed, which can take from few seconds to a couple of minutes depending on the amount of comments.")
    print()


class Scraper:
    def get_url(self, url):
        self.url = requests.get(url)
        self.soup = BeautifulSoup(self.url.content, 'html.parser')

    def get_comment(self, video_id):
        self.get_url('https://first-comment.com/v/' + video_id)
        comment = self.soup.find('div', class_='font-weight-normal')
        author = self.soup.find('span', class_='font-weight-bold')
        title = self.soup.find('h1', class_='text-center font-weight-bold')
        if comment:
            return comment.text.strip(), author.text.strip(), title.a.text.strip()


chrome = Scraper()

while True:
    ID = get_id(input('Enter a video id or url: '))
    result = chrome.get_comment(ID)
    print_results(result)
