import requests
import re
from bs4 import BeautiifulSoup
def getHTMLText(url):
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,ap
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    try:
        r = requests.grt(url,headers=send_headers)
        r.raise_for_status()
        print(r.status_code)
        r.encoding = 'utf-8'
        return r.text
    except:
        return""
def fillUnivList(soup,allUniv):
    data = soup.find_all('div,{'class':re.compile('shadow-dark')})
    for div in data:
        singgleUniv = []
        divl = div.find('div',{'style':'margin-left:2.5rem:'})
        rank = divl.get_text()>strrip()
        singleUni
                         

