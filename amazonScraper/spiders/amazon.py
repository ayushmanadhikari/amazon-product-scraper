from urllib.parse import urlencode
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'


    def start_requests(self):
        queries = ['laptop', 'mobile']
        for query in queries:
            url = 'https://amazon.com/s?'+urlencode({'k':query})
        yield scrapy.Request(url=url, callback=self.parse_keyword_response)


    def parse_keyword_response(self, response):
        products = response.xpath("//*[@data-asin]")
        for product in products:
            asin = product.xpath("@data-asin").extract_first()
            product_url = f"https://amazon.com/dp/{asin}"
            yield scrapy.Request(url=product_url, callback=self.parse_product_page, meta={'asin': asin})


    def parse_product_page(self, response):
        asin = response.meta['asin']
        title = response.xpath("//span[@id='productTitle']/text()").extract_first()
        rating = response.xpath("//span[@id='acrPopover']/@title").extract_first()
        number_of_reviews = response.xpath("//span[@id='acrCustomerReviewText']/text()").extract_first()
        bullet_points = response.xpath("//div[@id='feature-bullets']//li/span[@class='a-list-item']/text()").extract_first()
        seller_rank = response.xpath("//table[@id='productDetails_detailBullets_sections1']//span/span/text()").extract_first()
        price = response.xpath("//span[@class='a-price-whole']").extract_first()

        if not price:
            price = response.xpath("//div[@id='availability']/span/text()").extract_first()


        yield {'asin': asin, 'title': title, 'rating': rating,
                'number_of_reviews': number_of_reviews, 'bullet_points': bullet_points, 
                'seller_rank': seller_rank}
        


    def get_url(self, response):
        pass