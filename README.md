# 4chan_scraper
Scrapy based tool to grab all 4chan posts.

## Requirements
You would need to have scrapy installed in order to run this scraper.

`pip install scrapy`

The current code is based on MongoDB. You should install it before you run the spider. Otherwise you would need to "bend" the pipline into another direction like a filesystem ([Write to JSON File with scrapy](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#write-items-to-a-json-file))

* [Download MongoDB Community Edition](https://www.mongodb.com/download-center?#community)
* [Download MongoDB Compass Community Edition](https://www.mongodb.com/download-center?jmp=docs&_ga=2.106487491.1393936996.1528917700-864404028.1518123586#compass)

The later one is similiar to phpMyAdmin and MySQL databases. You can see the results of your scraper inside of the MongoDB server.
## Installation
Just download the whole project via git clone:

`git clone https://github.com/ihgalis/4chan_scraper.git`

## Let the spider crawl
Switch to the folder where you have downloaded the files and execute with scrapy. And execute the following:

```
cd your_install_directory
scrapy runspider spiders\four_chan
```


