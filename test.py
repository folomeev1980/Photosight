import os
from PIL import Image
from PhotosightDef import only_adult, adult_input, pic_download, remove_zerofiles,files_remove,size
days = 1  # Колличество дней назад
filesize = 307200  # Файлы меньшего размера будут удаляться
links = adult_input(False, days)  # Выбираем значение Adult: True или False
linksAdult = only_adult(days)
picDist = "d:\\ONEDRIVE\\Pictures\\Photosight\\"  # Папка записи файлов
rotation = 1.5  # Отношение ширины, высоты для фотографии


pic_download(links, linksAdult, picDist, rotation)

#files_remove("d:\\ONEDRIVE\\Pictures\\Photosight\\", 390)





# if __name__ == '__main__':
#     path = "d:\\ONEDRIVE\\Pictures\\Photosight\\"
#     size(path)
 # server.run(host="0.0.0.0", port=os.environ.get('PORT', 8443))
 # server = Flask(__name__)
#server.run(host='0.0.0.0', port=port)
