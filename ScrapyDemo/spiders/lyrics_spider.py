# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import Spider
from urllib.parse import urljoin
from items import ScrapydemoItem


class LyricsSpider(Spider):
    name = 'nw_lyrics'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36 Edg/79.0.309.56',
    }

    def start_requests(self):
        start_urls = 'https://www.azlyrics.com/n/nightwish.html'
        yield Request(start_urls, headers=self.headers)

    def parse(self, response):
        item = ScrapydemoItem()

        next_urls = response.xpath('//*[@id="listAlbum"]/div/a//@href').extract()
        for next_url in next_urls:
            next_url = urljoin(response.url, next_url)
            print(next_url)
            yield Request(next_url, headers=self.headers)

        song_lyrics = response.xpath('/html/body/div[3]/div/div[2]/div[5]/text').extract()
        song_name = response.xpath('/html/body/div[3]/div/div[2]/b/text').extract()
        item['song_name'] = song_name
        item['song_lyrics'] = song_lyrics
        yield item
