#!/usr/bin/env python3

import logging
import sys
import certifi
import requests
import argparse
from bs4 import BeautifulSoup as bsp
from requests.packages.urllib3.exceptions import InsecureRequestWarning


#configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


#disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



#ca_bundle_path=certifi.where()


#defining url schemes
forward_schemes=("http","ftp","mailto","file","data")
backward_schemes=(".php",".png",".jpeg",".jpg",".css",".xml",".html",".js",".gif",".csv",".svg",".mp3",".mp4",".zip",".txt",".doc",".docx",".pdf")


tags = ("img", "rel", "a")
attrs = ("href", "src")
#verify ssl certificates uncomment
#link=requests.get(args.link,verify=ca_bundle_path)


def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('-l','--link',required = True,  help="enter link to scrape")
    parser.add_argument('-sd','--ssld', action="store_true", help="disable ssl verification")
    parser.add_argument('-f', '--file',required = True,  action="store_true", help="find files")
    return parser.parse_args()



def ssl_verification_handler(args):
    try:
        if args.ssld:
            link=requests.get(args.link, verify=False)
            print("SSL verification disabled!")
            main_parser(link , args)
        #link=requests.get(args.link,verify=ca_bundle_path)
        else:
            link=requests.get(args.link, verify=True)
            print("SSL verfication enabled!\n")
            main_parser(link, args)
    
    except requests.exceptions.SSLError as ssl_error:
        print("SSL verification error:", ssl_error)
    except requests.exceptions.RequestException as request_error:
        print("An error occurred while making the request:", request_error)



#def parser(link):
#    soup=bsp(link.text,"html.parser")
#    urls=soup.find_all('a')
#    for url in urls:
#        href=url.get("href")
#        #print(href)
#        if href and (href.startswith(forward_schemes) or href.endswith(backward_schemes)):
#            print(href.startswith(forward_schemes))
#            print(href)
#            #logging.info(href)
#
##print(link.text)


def main_parser(link, args):
    print("start main parser")
    soup = bsp(link.text, "html.parser")
    urls = set()
    if args.file:
        backward_parser(link, soup, urls)
    else:
        forward_parser(link, soup, urls)
    print("done main parser")

def forward_parser(link, soup, urls):
    for link in soup.find_all(tags):
        href = link.get_all(attrs)
        if href:
            if href.startswith(forward_schemes):
                for scheme in forward_schemes:
                    if href.startswith(scheme):
                        logging.info(f"{href} (Scheme: {scheme})")
                        urls.add(href)
                        break
    return urls

def backward_parser(link, soup, urls):
    print("start backward parser")
    for link in soup.find_all(tags):
        for attr in attrs: 
            href = link.get(attr)
            if href:
                if href.endswith(backward_schemes):
                    for scheme in backward_schemes:
                        if href.endswith(scheme):
                            logging.info(f"{href} (Scheme: {scheme})")
                            urls.add(href)
                            break
    print("return backward parser")
    return urls




def main():
    args=parse_args()
    link=requests.get(args.link)
    ssl_verification_handler(args)
    



if __name__ == "__main__":
    main()
