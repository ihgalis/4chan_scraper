# -*- coding: utf-8 -*-
import scrapy
from four_chan_scrapy.items import FourChanScrapyItem
import hashlib


class FourChanSpider(scrapy.Spider):
    name = 'four_chan'
    start_urls = ['http://www.4chan.org/']

    def parse(self, response):
        # Alle Subboards finden
        for board in response.css("li a::attr(href) ").re(r"boards\.4chan\.org\/[a-z]{1,}"):
            page = 1

            # Durch alle Subseiten iterieren
            while (page < 10):
                page += 1
                yield scrapy.Request(url="http://"+board+"/"+str(page), callback=self.parse_board)


    def parse_board(self, response):
        # Durch jeden Thread gehen
        board_short = response.css("title::text").re(r"\/[a-z]{1,}\/")

        for thread in response.css("span.summary a::attr(href)").extract():
            yield scrapy.Request(url="http://boards.4chan.org"+board_short[0]+thread, callback=self.parse_thread)


    def parse_thread(self, response):
        # Aktuelles Board auslesen
        currentboard = response.css("div.boardTitle::text").extract_first()

        counter = 0
        # Durch jeden Post gehen
        for post in response.css("div.postContainer"):
            fcpost = FourChanScrapyItem()

            fcpost['board'] = currentboard

            datetime = post.css("span.dateTime::text").extract_first()
            fcpost['datetime'] = datetime

            posttext = post.css("blockquote.postMessage::text").extract_first()
            fcpost['posttext'] = posttext

            tohash = str(currentboard)+str(datetime)+str(posttext)
            hobject = hashlib.sha256(tohash.encode())
            fcpost['identityhash'] = str(hobject.hexdigest())

            postnum = post.css("span.postNum a::text").extract()
            fcpost['postnum'] = str(postnum[1])

            counter += 1
            # save data
            yield fcpost
