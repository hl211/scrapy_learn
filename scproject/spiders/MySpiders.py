from scrapy import Spider, Request, Selector

from scproject.items import ScprojectItem
from scproject.spiders.util.getDataFromMysql import mySqlData


class YscSpider(Spider):
    name = "ysc"
   # start_urls = ["http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml"]

    def start_requests(self):
        #蔬菜
        par_craft_index="13075"
        #shop
        craft_index=""
        #省
        par_p_index=""
        #市场
        p_index=""
        requests=[]
        url = "http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?" \
                  "par_craft_index=13075" \
                  "&craft_index=20413" \
                  "&par_p_index=53&" \
                  "p_index=21081&" \
                  "startTime=2017-01-01&" \
                  "endTime=2017-04-01"
        request = Request(url, callback=self.first_parse_item)
        requests.append(request)
        return requests


    def first_parse_item(self, response):
        sel=Selector(response)
        trs=sel.xpath('//section/div/div[1]/table/tr')
        times =trs.xpath("td[1]/text()").extract()
        prices=trs.xpath("td[3]/span/text()").extract()
        for index ,tt in  enumerate(times):
            res_item = ScprojectItem()
            res_item['time']=tt
            res_item['price']=prices[index]
            res_item['sid']='1111'
            res_item['mid']='111111'
            yield res_item
        page=sel.re(r'var v_PageCount = (\d*);')
        surl=response.url+'&page=%d'
        if not page is None :
            for x in range(2,int(page[0])+1):
                url = surl% x
                print (url)
                yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        sel=Selector(response)
        trs=sel.xpath('//section/div/div[1]/table/tr')
        times =trs.xpath("td[1]/text()").extract()
        prices=trs.xpath("td[3]/span/text()").extract()
        for index ,tt in enumerate(times):
            res_item = ScprojectItem()
            res_item['time']=tt
            res_item['price']=prices[index]
            res_item['sid']='1111'
            res_item['mid']='111111'
            yield res_item