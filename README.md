# amazon-product-scraper

#### A project to scrape https://www.amazon.com/ for the products of your choice. 
#### Simply pull the repo or download the zip file and create a virtual environment by installing the modules specified in the requirements.txt. 
#### Then use the following commands to start scraping Amazon.




###Use the following syntax to scrape for any query of your choice

``` scrapy crawl amazon -a query="your_query"  ```

#### Example:
```  scrapy crawl amazon -a query="gaming laptop" ```


#### This will search amazon for the keyword "gaming laptop" and return you the result which contains it's product id, product name, price, rating and seller's rank in the terminal. If you want to extract the output to some file, you can add one more parameter as:

``` scrapy crawl amazon -o filename.extension -a query="your_query" ```

#### Example:
``` scrapy crawl amazon -o gaming_laptop.csv -a query="gaming laptop"
