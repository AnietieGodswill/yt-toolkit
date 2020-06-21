###############################################################
from bs4 import BeautifulSoup as bs
import re
import urllib.request
import requests
import wget
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
###############################################################
inpurl = input("Enter a URL: ")
url1 = urllib.request.urlopen(inpurl).read().decode('utf-8')


titles = re.findall('<meta property="og:title" content="(.+)">',url1)
for title in titles:
    print('-------------------------------------------------------------------------------------------------------')
    print(f'Title URL: {title}')
'''
#for views
startsWithURL = '"viewCount":{"simpleText":"'
endsWithURL = '"},"shortViewCount"'
joinURL = url1[url1.find(startsWithURL)+len(startsWithURL):url1.rfind(endsWithURL)]
print(joinURL)
'''
print('-------------------------------------------------------------------------------------------------------')

descs = re.findall('<meta property="og:description" content="(.+)">',url1)
for desc in descs:
    print(f'Description: {desc.translate(non_bmp_map)}')
    print('-------------------------------------------------------------------------------------------------------')

print("1|YT THUMBNAIL DOWNLOADER")
print("2|TAGS FROM VIDEOS")
search = int(input("CHOOSE: "))
if search == 1:
    images = re.findall('<meta property="og:image" content="(.+)">',url1)
    for image in images:
        print(f'Thumbnail URL: {image}')
        downloadImage = wget.download(image)
        print(downloadImage)

elif search == 2:
    tags = re.findall('<meta property="og:video:tag" content="(.+)">',url1)
    for tag in tags:
        print(tag,end=",")

    
