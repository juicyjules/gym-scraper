from bs4 import BeautifulSoup
import requests
from lxml import etree

class Scraper():
    def __init__(self,url):
        self.url = url


    def html(self):
        req = requests.get(self.url)
        html = BeautifulSoup(req.content,"html.parser")
        return html

    def isolate(self,target):
        html = self.html()
        documentObjectModel = etree.HTML(str(html))
        return documentObjectModel.xpath(target)