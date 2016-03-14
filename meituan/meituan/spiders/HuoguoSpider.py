# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
import urllib2

from scrapy import Selector
from json import JSONDecoder
import scrapy
from .. import items


# 美团爬虫
class HuoguoSpider(scrapy.Spider):

    def __init__(self):
        self.page = 1

    limit_page = 10
    name = "huoguo"
    allowed_domain = ["cd.meituan.com"]
    start_urls = [
        "http://cd.meituan.com/category/huoguo/all/page{}?mtt=1.index%2Fdefault%2Fpoi.0.0.ilp7aqrm".format(str(page))
        for page in range(limit_page)]

    def parse(self, response):
        hxs = Selector(response)
        action = hxs.xpath('//div[@class="J-scrollloader cf J-hub"]/@data-async-params').extract()
        param = JSONDecoder().decode(eval(str(action[0]))['data'])
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
            "Connection": "keep-alive",
            "Cookie": "uuid=4ec469314c24592c17d4.1457786900.1.0.1; oc=K-biRgRZ5w1i5DPhik_ANdx0dQf5qEKDnpGtgE10DmOaN6lqDPDGb2SjhoDfpABTuN7vGfc6Jf0s8Q9z00EmCQBqpaHYO_Gpch5_kOuKmRnZAtrTlN7q2xHhIT22KNbViH_IEC8QXpHcc0r-mBBslUw5I0ipRLwxfw6EnGMTTXk; ci=59; abt=1457786900.0%7CBCF; __utma=211559370.120142566.1457786838.1457786838.1457788290.2; __utmc=211559370; __utmz=211559370.1457786838.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=211559370.|1=city=cd=1; __mta=216856489.1457786837515.1457790956603.1457791296341.24; SID=fkg0imnrl0sv7h9n0injiddrg0; n=IfV514662996; m=506496088%40qq.com; lt=tlHsPgWiAZDP4SUStAOUcytLFR8AAAAA7wEAAEUU-Lu_spj2xLegwKzOuMJktYV6ehYF6Vkul5io8zCwe3Y6MC0f7urhV4uNkPYdtA; lsu=506496088%40qq.com; token2=9RIWX0hMHy_3plNB6niiKTvHHUcAAAAA7gEAAB6s5X7Lqm9WEvhTD4SQc51C7onRESugoQ-mthyqxCjDUfkZuNMqmvEAQaQkaICh1w; u=127889406; em=bnVsbA; om=bnVsbA; ls=1457786960; vipnotice_127889406=%7B%22status%22%3Atrue%2C%22growthValue%22%3A629%2C%22showLevel%22%3A2%2C%22noticeType%22%3A0%2C%22noticeValue%22%3A0%2C%22cityid%22%3A59%7D; tipssecurequestion=1; ppos=38.0207%2C114.562651; pposn=%E9%87%8D%E5%BA%86%E7%A7%A6%E5%A6%88%E7%81%AB%E9%94%85%EF%BC%88%E8%A3%95%E5%8D%8E%E5%BA%97%EF%BC%89; rvct=76; __utmb=211559370.7.9.1457792016730",
            "Host": "cd.meituan.com",
            "Referer": "http://cd.meituan.com/category/huoguo/all/page{}?mtt=1.index%2Fdefault%2Fpoi.0.0.ilp73gir".format(
                self.page),
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
            "Content-Length": "0",
            "X-Requested-With": "XMLHttpRequest"
        }
        param_dic = {
            "bigImageMode": str(param['bigImageMode']).replace("u'", "'").replace("\\", ""),
            "poiData": str(param['poiData']).replace("u'", "'").replace("\\", ""),
            "poiidList": str(param['poiidList']).replace("u'", "'").replace("\\", "")
        }
        my_request = urllib2.Request("http://cd.meituan.com/index/poilist")
        my_request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
        my_request.add_header("Accept-Language", "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3")
        my_request.add_header("Connection", "keep-alive")
        my_request.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
        my_request.add_header("Cookie",
                              "uuid4ec469314c24592c17d4=.1457786900.1.0.1; oc=K-biRgRZ5w1i5DPhik_ANdx0dQf5qEKDnpGtgE10DmOaN6lqDPDGb2SjhoDfpABTuN7vGfc6Jf0s8Q9z00EmCQBqpaHYO_Gpch5_kOuKmRnZAtrTlN7q2xHhIT22KNbViH_IEC8QXpHcc0r-mBBslUw5I0ipRLwxfw6EnGMTTXk; ci=59; abt=1457786900.0%7CBCF; __utma=211559370.120142566.1457786838.1457786838.1457788290.2; __utmc=211559370; __utmz=211559370.1457786838.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=211559370.|1=city=cd=1; __mta=216856489.1457786837515.1457790956603.1457791296341.24; SID=fkg0imnrl0sv7h9n0injiddrg0; n=IfV514662996; m=506496088%40qq.com; lt=tlHsPgWiAZDP4SUStAOUcytLFR8AAAAA7wEAAEUU-Lu_spj2xLegwKzOuMJktYV6ehYF6Vkul5io8zCwe3Y6MC0f7urhV4uNkPYdtA; lsu=506496088%40qq.com; token2=9RIWX0hMHy_3plNB6niiKTvHHUcAAAAA7gEAAB6s5X7Lqm9WEvhTD4SQc51C7onRESugoQ-mthyqxCjDUfkZuNMqmvEAQaQkaICh1w; u=127889406; em=bnVsbA; om=bnVsbA; ls=1457786960; vipnotice_127889406=%7B%22status%22%3Atrue%2C%22growthValue%22%3A629%2C%22showLevel%22%3A2%2C%22noticeType%22%3A0%2C%22noticeValue%22%3A0%2C%22cityid%22%3A59%7D; tipssecurequestion=1; ppos=38.0207%2C114.562651; pposn=%E9%87%8D%E5%BA%86%E7%A7%A6%E5%A6%88%E7%81%AB%E9%94%85%EF%BC%88%E8%A3%95%E5%8D%8E%E5%BA%97%EF%BC%89; rvct=76; __utmb=211559370.7.9.1457792016730")
        my_request.add_header("Host", "cd.meituan.com")
        my_request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0")
        my_request.add_header("Referer",
                              "http://cd.meituan.com/category/huoguo/all/page{}?mtt=1.index%2Fdefault%2Fpoi.0.0.ilp7aqrm".format(
                                  self.page))
        my_request.add_header("X-Requested-With", "XMLHttpRequest")
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        opener.addheaders.append(('Cookie', headers.get("Cookie")))
        encode_param = urllib.urlencode(param_dic).replace("27", "22")
        my_response = opener.open(my_request, encode_param)
        result = my_response.read()
        html_str = eval(result)['data'].decode("unicode_escape").replace("\/", "/")
        my_select = Selector(text=html_str)
        shop_names = my_select.xpath('//div[@class="poi-tile__info"]/div[1]/a/text()').extract()
        counts = my_select.xpath('//div[@class="poi-tile__info"]/div[2]/div[2]/a/span/text()').extract()
        addrs = my_select.xpath('//div[@class="poi-tile__info"]/div[2]/div[1]/a[2]/text()').extract()
        for name, count, addr in zip(shop_names, counts, addrs):
            item = items.MeituanItem()
            item["name"] = name
            item["count"] = count
            item["addr"] = addr
            yield item

        count = self.page
        self.page = count + 1
