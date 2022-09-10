# amazon-product-scraper




###Use the following syntax to scrape for any query of your choice 

``` scrapy crawl amazon -a query="your_query"  ```
``` example: scrapy crawl amazon -a query="gaming laptop" ```


#### This will search amazon for the keyword "gaming laptop" and return you the result which contains it's product id, product name, price, rating and seller's rank.
#### in the terminal. If you want to extract the output to some file, you can add one more parameter as:

> scrapy crawl amazon -o filename.extension -a query="your_query"
> example: scrapy crawl amazon -o gaming_laptop.csv -a query="gaming laptop"

