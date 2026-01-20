#!/usr/bin/env python3


import os
import threading
import time
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
    datefmt="%H:%M:%S",
)


#disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



#ca_bundle_path=certifi.where()


#defining url schemes
forward_schemes=("http","ftp","mailto","file","data")
backward_schemes=(".php",".png",".jpeg",".jpg",".css",".xml",".html",".js",".gif",".csv",".svg",".mp3",".mp4",".zip",".txt",".doc",".docx",".pdf")


tags = ("img", "rel", "a", "link", "script", "video", "audio", "source", "embed", "object", "iframe", "form", "input")
attrs = ("href", "src", "srcset", "data", "action", "formaction", "manifestat", "poster", "xlink:href")

#verify ssl certificates uncomment
#link=requests.get(args.link,verify=ca_bundle_path)


def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('-l','--link',required = True,  help="enter link to scrape")
    parser.add_argument('-sd','--ssldisable', action="store_true", help="disable ssl verification")
    parser.add_argument('-b', '--backward',required = False,  action="store_true", help="runs backward parser, for files")
    parser.add_argument('-f', '--forward',required = False, action="store_true", help="runs forward parser, for files") 
    parser.add_argument('-t', '--timer', type = int, required = True, help="runs script for time in seconds")
    parser.add_argument('-wf', '--write',required = False,  action="store_true", help="writes output to file")
    #to add arguments
    parser.add_argument('-rc', '--recursivecrawl',required = False,  action="store_true", help="recursively crawls each link found")
    #logging.info(f"{parser}")
    #logging.info(f"{parser}")
    #logging.info(f"{parser}")
    #logging.info(f"{parser}")
    return parser.parse_args()



def ssl_verification_handler(args):
    try:
        if args.ssldisable:
            link=requests.get(args.link, verify=False) #verifies the servers TLS certificate
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


def generate_file_name(url, log_dest = "logs"):
    # Extract the base name from the URL
    base_name = os.path.basename(url)
    if not base_name:
        base_name = "output"
    file_name = os.path.join(log_dest, f"{base_name}.txt")
    return file_name

def main_parser(link, args):
    print("start main parser")
    soup = bsp(link.text, "html.parser")
    urls = set()
    file_name = generate_file_name(args.link)
    with open(file_name, "w+") as file:
        if args.backward:
            backward_parser(link, soup, urls, file)
        elif args.forward:
            forward_parser(link, soup, urls, file)
    print("done main parser")

def forward_parser(link, soup, urls, file):
    print("start forward parser")
    for link in soup.find_all(tags):
        for attr in attrs:
            href = link.get(attr)
            if href:
                if href.startswith(forward_schemes):
                    for scheme in forward_schemes:
                        if href.startswith(scheme):
                            text_buffer = f"{href} (Scheme: {scheme})"
                            logging.info(text_buffer)
                            file.write(text_buffer + "\n")
                            urls.add(href)
                            break
    print("end forward parser")
    sys.exit()
    #return urls

def backward_parser(link, soup, urls, file):
    print("start backward parser")
    for link in soup.find_all(tags):
        for attr in attrs: 
            href = link.get(attr)
            if href:
                if href.endswith(backward_schemes):
                    for scheme in backward_schemes:
                        if href.endswith(scheme):
                            text_buffer = f"{href} (Scheme: {scheme})"
                            logging.info(text_buffer)
                            file.write(text_buffer + "\n")
                            urls.add(href)
                            break
    print("return backward parser")
    sys.exit()
    #return urls



def main():
    args=parse_args()
    #manage_thread(args.timer)
    start_time = time.time()
    link=requests.get(args.link)
    ssl_verification_handler(args)
    while time.time() - start_time < args.timer:
        time.sleep(1)
    print("time limit exceeded, exiting")
    sys.exit()
    

def manage_thread(lifespan):
    #global stop_thread
    main_thread = threading.Thread(target = main)
    main_thread.start()
    print("thread started")
    #time.sleep(lifespan)
    #stop_thread = True
    main_thread.join(lifespan)
    if main_thread.is_alive():
        print("thread running, terminating now")
        sys.exit()
    print("thread stopped")



if __name__ == "__main__":
    args = parse_args()
    if args.timer:
        manage_thread(args.timer)
    else:
        sys.exit()
