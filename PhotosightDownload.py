from PhotosightDef import only_adult, adult_input, pic_download, remove_zerofiles,files_remove,size
from AdultClass import Photosight
#  -----------Переменные---------------------------------------------
#
days = 1  # Колличество дней назад
filesize = 307200  # Файлы меньшего размера будут удаляться
# links = adult_input(False, days)  # Выбираем значение Adult: True или False
# linksAdult = only_adult(days)
picDist = "d:\\ONEDRIVE\\Pictures\\Photosight\\"  # Папка записи файлов
rotation = 1.5  # Отношение ширины, высоты для фотографии
#   -------------Тело программы---------------------------------------
# print(links)
# if len(links) > 1:
#     try:
#         pic_download(links, linksAdult, picDist, rotation)
#     except Exception as e:
#         print(e)
#         print("Скачивание и запись файлов прошла с ошибками")
#         remove_zerofiles(picDist, filesize)

# else:
#     print("")
ph=Photosight(days,picDist,adult=False)
link=ph.parceLinks()
ph.downloader(link)

remove_zerofiles(picDist, filesize)
size(picDist)
files_remove(picDist,500)




