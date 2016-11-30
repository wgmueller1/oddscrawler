import scrapy

class BoxingOddsSpider(scrapy.Spider):
    name = "boxing_odds"
    allowed_domains = ["www.oddsportal.com"]
    start_urls = [
        "http://www.oddsportal.com/boxing/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)