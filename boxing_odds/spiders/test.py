import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
import json
from selenium import webdriver
import time

class MyItem(Item):
    name = Field()
    link = Field()
    time = Field()
    date = Field()
    result = Field()
    fight = Field()
    win1 = Field()
    draw = Field()
    win2 = Field()
    bookmakers = Field()


def print_this_link(self, link):
        print "Link --> {this_link}".format(this_link=link)

class BoxingOddsSpider(CrawlSpider):
    name = "boxing_odds"
    allowed_domains = ['www.oddsportal.com']
    start_urls = [
        "http://www.oddsportal.com/boxing/world/welterweight-wbc-title-men-2010/results/"
    ]
    driver = webdriver.Firefox()
    rules = (Rule(LinkExtractor(allow=r'/boxing'), callback='parse_obj', follow=True),)

    def parse_obj(self,response):
        self.driver.get(response.url)
        time.sleep(5)

        hxs = Selector(response)
        #rows = self.driver.find_element_by_xpath('//table[@id="tournamentTable"]/tbody/tr[@class="odd deactivate"]')
        table = self.driver.find_element_by_xpath('//table[@id="tournamentTable"]')
        all_rows1 = table.find_elements_by_xpath('//tr[@class="center nob-border"]')
        if 'results' in response.url:
            all_rows2 = table.find_elements_by_xpath('//tr[@class="odd deactivate"]')
        else:
            all_rows2 = table.find_elements_by_xpath('//table[@id="tournamentTable"]//tr[@class="odd"]')

        item = MyItem()
        item['date']=[]
        item['time']=[]
        item['fight']=[]
        item['result']=[]
        item['win1']=[]
        item['draw']=[]
        item['win2']=[]
        item['bookmakers']=[]

        for rows in all_rows1:
            dat=rows.text.split()
            item['date'].append(' '.join(dat[0:3]))
        
        for rows in all_rows2:
            dat=rows.text.split('\n')
            try:
                #item['time'].append(dat[0])
                item['fight'].append(dat[0])
                #item['result'].append(dat[1])
                item['win1'].append(dat[1])
                item['draw'].append(dat[2])
                item['win2'].append(dat[3])
                item['bookmakers'].append(dat[4])
            except IndexError:
                pass

        #print(rows.text)
        #for row in rows:
        #    print(row)
        #    print('\n')
  
        item['link'] = []
        item['name'] = []

        # for link in LinkExtractor(allow =self.allowed_domains).extract_links(response):
        #     if all(word in link.url for word in ['boxing','results']):
        #         item['link'].append(link.url)
        #         item['name'].append(link.url)
        #         filename="/Users/k25611/code/boxing_odds/boxing.html"
        #         with open(filename, 'wb') as f:
        #             f.write(response.body)
        #     else:
        #        pass
        return item

        self.driver.close()


        #    for link in LxmlLinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
        #        item['url'].append(link.url)
        #        f.write(link.url+'\n')
        #f.close()