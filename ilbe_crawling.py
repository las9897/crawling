from bs4 import BeautifulSoup
import requests


def crawling(url):
    code = requests.get(url)
    plainText = code.text
    soup = BeautifulSoup(plainText, 'lxml')    
    for data in soup.select("#content > div.content_margin > form > table > tbody > tr:nth-child(5) > td.title.bdoc_10740911032 > a"):
        print(data.get('href'))
        



crawling("http://www.ilbe.com/index.php?mid=ilbe&page=1")