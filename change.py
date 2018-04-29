# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import os
import re
def mylistdir(p,f):
    a=os.listdir(p)
    fs=myfind(a,f)
    return(fs)
def myfind(l,p):
    lr=[];
    #print p
    p1=p.replace(".",r"\.")
    p2=p1.replace("*",".*")
    p2=p2+"$"
    p2="^"+p2
    for a in l:
        #print a
        if  re.search(p2,a,re.IGNORECASE)==None :
           pass
           #print "pass"
        else:
           lr.append(a)
       #print "append"
    return lr
def change(f):
    if os.path.isdir(f):
        changedir(f)
    return
def changedir(f):
    content=open(f+"/index.html").read()
    soup = BeautifulSoup(content,"html.parser")
    ass=soup.find_all('a')
    links=soup.find_all('link')
    links=links+ass
    for a1 in links:
        href=a1.attrs["href"]
        if ".com" in href:
            a1.attrs["href"]="#"
            pass
        elif ".org" in href:
            a1.attrs["href"]="#"
            pass
        else:
            if href[0]=="/":
                a1.attrs["href"]="./"+href
    imgs=soup.find_all('img')
    iframes=soup.find_all('iframe')
    imgs=imgs+iframes
    for a1 in imgs:
        href=a1.attrs["src"]
        if ".com" in href:
            a1.attrs["src"]="#"
            pass
        elif ".org" in href:
            a1.attrs["src"]="#"
            pass
        else:
            if href[0]=="/":
                a1.attrs["src"]="./"+href
    scripts=soup.find_all('script')
    for a1 in scripts:
        a1.clear()
    print("out/"+f)
    file=open("out/"+f,"w")
    file.write(str(soup))
    file.close()
    return
def main():
    fs=mylistdir(".","*.html")
    for f in fs:
        change(f)
if __name__=="__main__":
    main()