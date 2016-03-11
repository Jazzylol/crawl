#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector


class TripSpider(scrapy.Spider):
    name = "trip"
    allowed_domain = ["http://www.tripadvisor.cn"]
    start_urls = ["http://www.tripadvisor.cn/Attractions-g308272-Activities-oa90-Shanghai.html"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        print hxs
        # web_data = BeautifulSoup(response.text)
        # print(web_data)

        # for url in start_urls:
        #     print(url)
        # response = requests.get(url)
        # txt = response.data
        # print(txt)
        # response = Request(url)
        # print hxs
        # print(response.body)
        # soup = BeautifulSoup(response.text, 'lxml')
        # print(soup)
