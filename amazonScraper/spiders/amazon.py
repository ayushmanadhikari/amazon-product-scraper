from itertools import count
import keyword
from urllib.parse import urlencode, urljoin
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'

    #starting point of the scraping project.. queries block contains the list of queries/keywords to search amazon for 
    #this method then in turn calls the parse keyword response method with scrapes the data from the product's list page
    def start_requests(self):
        query = getattr(self, 'query', None)
        if keyword is not None:
            url =  'https://amazon.com/s?'+urlencode({'k':query})
        
        #replace the code above with the below code to enter the search keyword here instead of through the terminal
        #queries = ['rubiks cube','magic cube', 'speed cube']
        #for query in queries:
        #    url = 'https://amazon.com/s?'+urlencode({'k':query})

        yield scrapy.Request(url=url, callback=self.parse_keyword_response)


    #this method scrapes the products list page and extracts data-asin, which is the product's id
    #this data-asin is used to follow product's page and extract each product's data 
    def parse_keyword_response(self, response):
        products = response.xpath("//*[@data-asin]")
        count = 0
        for product in products:
            count = count + 1
            asin = product.xpath("@data-asin").extract_first()
            product_url = f"https://amazon.com/dp/{asin}"
            yield scrapy.Request(url=product_url, callback=self.parse_product_page, meta={'asin': asin})
        
        #counts the number of product in each page
        print(str(count)+" products found in page")

        #to follow all the products listing pages from 1st to last
        next_page = response.xpath("//a[contains(text(), 'Next')]/@href").extract_first()
        if next_page:
            url = urljoin('https://www.amazon.com', next_page)
            yield scrapy.Request(url=url, callback=self.parse_keyword_response)


    #this method extracts the product info from the product's specific page
    def parse_product_page(self, response):
        asin = response.meta['asin']
        title = response.xpath("//span[@id='productTitle']/text()").extract_first()
        rating = response.xpath("//span[@id='acrPopover']/@title").extract_first()
        number_of_reviews = response.xpath("//span[@id='acrCustomerReviewText']/text()").extract_first()
        bullet_points = response.xpath("//div[@id='feature-bullets']//li/span[@class='a-list-item']/text()").extract_first()
        seller_rank = response.xpath("//table[@id='productDetails_detailBullets_sections1']//span/span/text()").extract_first()
        price = response.xpath("//span[@class='a-price-whole']/text()").extract_first()
        if not price:
            price = response.xpath("//div[@id='availability']/span/text()").extract_first()
        

        yield {'asin': asin, 'title': title, 'price':price, 'rating': rating,
                'number_of_reviews': number_of_reviews, 'bullet_points': bullet_points, 
                'seller_rank': seller_rank}
        


    def get_url(self, response):
        pass