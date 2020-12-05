import requests
import datetime
import os

from PIL import Image


# https://cdn.photosight.ru/img/a/cd4/6980056_xlarge.jpg

def adult_input(zeroOrone, days):
    proxies = {
        'https': 'http://10.104.1.9:8080', }
    now = datetime.datetime.now()
    i = 0
    links = []
    cooc = {'adult_mode': '1'}
    photosight = "https://photosight.ru/outrun/date/" + str(now.year) + "/" + str(now.month) + "/" + str(
        now.day - days) + "/"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
    #print(photosight)




    try:
        if zeroOrone == True:
            response = requests.get(photosight, headers=headers, cookies=cooc)
            # print(response.content)
        else:
            response = requests.get(photosight, headers=headers)
    except Exception as e:
        if "[WinError 10061]" in str(e):
            if zeroOrone:
                response = requests.get(photosight, headers=headers, proxies=proxies,cookies=cooc)
            else:
                response = requests.get(photosight, headers=headers, proxies=proxies)





    if response.status_code == 200:
        response.encoding
        'utf-8'
        txt = response.text

        # https://cdn.photosight.ru/img/b/96e/7051258_xlarge.jpg

        count = txt.count("https://cdn")
        while i <= count - 1:
            b = txt.find("https://cdn")
            print(txt[b:b + 39] + "_xlarge.jpg")
            links.append(txt[b:b + 43] + "_xlarge.jpg")
            txt = txt[b + 44:]
            i = i + 1

    else:
        print("Нет доступа к сайту")
    links = links[1:-2]
    # print(links)
    return links


def only_adult(days):
    a = adult_input(True, days)
    b = adult_input(False, days)
    adultLinks = []
    for i in a:
        if i not in b:
            adultLinks.append(i)
    return adultLinks


def pic_download(links, linksAdult, picDist, rotation):
    print(links,linksAdult)
    print("Начало скачивания")
    j = 0
    k = 0

    while j < len(links):

        if links[j] in linksAdult:
            f = open(picDist + links[j][-18:-12] + "_adult" + ".jpg", "wb")  # открываем файл для записи, в режиме wb
        else:
            f = open(picDist + links[j][-18:-12] + ".jpg", "wb")
        ufr = requests.get(str(links[j]))  # делаем запрос
        f.write(ufr.content)
        f.close()
        j = j + 1

    while k < len(links):
        if links[k] in linksAdult:
            filepath = picDist + links[k][-18:-12] + "_adult" + ".jpg"
        else:
            filepath = picDist + links[k][-18:-12] + ".jpg"
        with Image.open(filepath) as img:
            width, height = img.size

        # if (width / height) < rotation:
        #     os.remove(filepath)
        # else:
        print("Файл скачан: " + filepath, "(", width, height, ")", "{0:.2f}".format(width / height))
        k = k + 1


def remove_zerofiles(picDist, size):
    a = os.listdir(picDist)
    for i in a:
        if os.path.getsize(picDist + i) < size:
            os.remove(picDist + i)
        elif os.path.isfile(picDist + i) != True:
            os.remove(picDist + i)


def files_remove(path: str, max_number=350):
    path = "d:\\ONEDRIVE\\Pictures\\Photosight\\"
    remlist = []
    rem_files = []  # список файлов  для удаления
    num_files = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path))
    if num_files > max_number:  # вывод колличества файлов в папке path

        n = num_files - max_number
        print(n)

        files = os.listdir(path)
        for i in range(n):
            remlist.append(files[i])

        for j in remlist:
            os.remove(path + j)
            print(path + j)
        print("Файлы удалены")

    else:

        print("Колличество файлов не привышает заданное")


def size(path):
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        with Image.open(filepath) as im:
            x, y = im.size
        totalsize = x / y
        # print(totalsize)
        if totalsize < 1.49 or totalsize > 1.75:
            os.remove(filepath)
