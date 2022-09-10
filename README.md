# amazon-product-scraper

### A project to scrape https://www.amazon.com/ for the products of your choice. 
### Simply pull the repo or download the zip file and start scraping Amazon.
### Create a virtual environment by installing the modules specified in the requirements.txt. 
### Then use the following commands to start scraping Amazon.




###Use the following syntax to scrape for any query of your choice

``` scrapy crawl amazon -a query="your_query"  ```

#### Example:
```  scrapy crawl amazon -a query="gaming laptop" ```


#### This will search amazon for the keyword "gaming laptop" and return you the result which contains it's product id, product name, price, rating and seller's rank.
#### in the terminal. If you want to extract the output to some file, you can add one more parameter as:

``` scrapy crawl amazon -o filename.extension -a query="your_query" ```

#### Example:
``` scrapy crawl a





















^G Get Help                       ^O WriteOut                       ^R Read File                      ^Y Prev Pg                        ^K Cut Text                       ^C Cur Pos
^X Exit                           ^J Justify                        ^W Where is                       ^V Next Pg                        ^U UnCut Text                     ^T To Spell