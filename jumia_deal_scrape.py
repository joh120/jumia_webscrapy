import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

# Creates the Spider class

class Jumia(scrapy.Spider):
 name = "jumia"
 # start_requests method
 def start_requests(self):
    url_top_deals = "https://www.jumia.co.ke/mlp-electro-shock/"
    yield scrapy.Request(url = url_top_deals,
    callback = self.parse_front)

 # A parsing method
 def parse_front(self, response):
    deal_box = response.css('article.prd _box col _hvr')
    jumia_deal_links = deal_box.xpath('./a/@href')
    link_deal_crawl = jumia_deal_links.extract()
    for url in link_deal_crawl:
        yield response.follow(url = url,
        callback = self.parse_pages)

 # A second parsing method
 def parse_pages(self, response):
 #global jumia_dict
    price_of_product = response.xpath('//div[contains(@class,"df -i-ctr -fw-w -pas -brbl-fsale -rad4-bot")]/text()')
    price_dict ["price"] = price_of_product
    deal_brand_desc = response.xpath('//h1[contains(@class,"-fs20 -pts -pbxs")]/text()')
    deal_brand_desc_value = deal_brand_desc.extract_first().strip()
    rating_review_desc = response.css('div.stars _m _al::text')
    rating_review_desc_value = [rating_review_desc.strip() for rating_review_desc in rating_review_desc.extract()]
    jumia_dict[ deal_brand_desc_value ] = rating_review_desc_value

# Initialize the dictionary **outside** of the Spider class
price_dict = dict()
jumia_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(Jumia)
process.start()

# Define the price_of_deals and jumia_deal_card function
def price_of_deals(price_dict):
    for price in price_dict:
        print(f"price of deal from start to fiinsh on top deals is {price}")

def jumia_deal_card(jumia_dict):
 for deal_brand_desc, rating_review_desc in jumia_dict.items():
    return (f"The deal/ brand description and review/ratings: {deal_brand_desc} , {rating_review_desc}")


jumia_deal_card(jumia_dict) 

