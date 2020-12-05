import requests
import datetime
import os
from bs4 import BeautifulSoup
from PIL import Image



class Photosight():
    proxies = {'https': 'http://10.104.1.9:8080', }
    cooc = {'adult_mode': '1'}
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)

    def __init__(self, days, pic_dist, adult=True):
        self.days = days
        self.pic_dist = pic_dist
        self.adult = adult

    def parceLinks(self, ):

        # photosight = "https://photosight.ru/outrun/date/" + self.year + "/" + self.month + "/" + str(
        #     int(self.day) - self.days) + "/"
        photosight="https://photosight.ru/best/?time=day"




        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
        print(photosight)
        try:

            response_adult = requests.get(photosight, headers=headers, cookies=self.cooc)
            response = requests.get(photosight, headers=headers)
        except Exception as e:
            if "[WinError 10061]" in str(e):
                response_adult = requests.get(photosight, headers=headers, proxies=self.proxies, cookies=self.cooc)
                response = requests.get(photosight, headers=headers, proxies=self.proxies)

        if response.status_code == 200 and response_adult.status_code == 200:
            response = response.content
            response_adult = response_adult.content
            simple = BeautifulSoup(response, "lxml")
            adult = BeautifulSoup(response_adult, "lxml")
            simple = simple.find_all("div", class_="photo-item cols-item")
            link_simple = ["https://cdn.photosight.ru/img" + s.find("img")["src"].replace(".jpg", "_xlarge.jpg")[-25:]
                           for s in simple]
            adult = adult.find_all("div", class_="photo-item cols-item")
            link_adult = ["https://cdn.photosight.ru/img" + s.find("img")["src"].replace(".jpg", "_xlarge.jpg")[-25:]
                          for s in adult]
            link_adult = list(set(link_adult) - set(link_simple))
            return [link_adult, link_simple]

        else:
            print("Oops")

    def downloader(self, link):

        if self.adult:
            link_ = link[0] + link[1]
        else:
            link_ = link[1]
        print("{} files in the link list".format(len(link_)))
        for l in link_:

            if l not in link[0]:
                l_ = self.pic_dist + l[-18:-11] + "_{}{}{}{}".format(self.day, self.month, self.year, ".jpg")
            else:
                l_ = self.pic_dist + l[-18:-11] + "_{}{}{}{}".format(self.day, self.month, self.year, "_adult.jpg")

            with open(l_, "wb") as f:
                try:
                    ufr = requests.get(l)
                except Exception as e:
                    if "[WinError 10061]" in str(e):
                        ufr = requests.get(l, proxies=self.proxies)
                f.write(ufr.content)
                print("Write", l_)
#
#
# if __name__ == "__main__":
#     ph = Photosight(1, "")
#     link_adult, link_simple = ph.parceLinks()
#     print(link_adult)
