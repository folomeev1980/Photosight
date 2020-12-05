url="http://www.photosight.ru/outrun/date/2020/6/3/"
import requests
proxies = {'https': 'http://10.104.1.9:8080',}
r=requests.get(url, proxies=proxies)
print(r.content)