#!/usr/bin/env python3

import certifi
import requests
import argparse
from bs4 import BeautifulSoup as bsp

#ca_bundle_path=certifi.where()
forward_schemes=("http","ftp","mailto","file","data")
backward_schemes=(".php",".png",".jpeg",".jpg",".css",".xml",".html",".js",".gif",".csv",".svg",".mp3",".mp4",".zip",".txt",".doc",".docx",".pdf")
parser=argparse.ArgumentParser()
parser.add_argument("link", help="enter link to scrape")
args=parser.parse_args()
link=requests.get(args.link)
#link=requests.get(args.link,verify=ca_bundle_path)
soup=bsp(link.text,"html.parser")
urls=soup.find_all('a')
for url in urls:
    href=url.get("href")
    print(href)
    if href and href.startswith(forward_schemes):
        print(href)
    if href and href.endswith(backward_schemes):
        print(href)



#print(link.text)


