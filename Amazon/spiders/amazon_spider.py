# -*- coding: utf-8 -*-
# scraping amazon 8k and 4k tvs data 
import scrapy
from ..items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 2
    #allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?i=electronics&bbn=6459737011&rh=n%3A172282%2Cn%3A493964%2Cn%3A1266092011%2Cn%3A172659%2Cn%3A6459737011%2Cp_n_feature_keywords_three_browse-bin%3A19205588011%7C7688788011&dc&fst=as%3Aoff&qid=1589582978&rnid=7688787011&ref=sr_nr_p_n_feature_keywords_three_browse-bin_3'
        ]

    def parse(self, response):
        items = AmazonItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_category = response.css('.a-link-normal.a-text-bold').css('::text').extract() 
        product_price = response.css('.a-price-whole , .a-price-fraction').css('::text').extract() 
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_category'] = product_category
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink
        
        yield items

        next_page = 'https://www.amazon.com/s?i=electronics&bbn=6459737011&rh=n%3A172282%2Cn%3A493964%2Cn%3A1266092011%2Cn%3A172659%2Cn%3A6459737011%2Cp_n_feature_keywords_three_browse-bin%3A19205588011%7C7688788011&dc&page='+ str(AmazonSpiderSpider.page_number) + '&fst=as%3Aoff&qid=1589583281&rnid=7688787011&ref=sr_pg_'+ str(AmazonSpiderSpider.page_number) + ''
        if AmazonSpiderSpider.page_number is not None:
            AmazonSpiderSpider.page_number +=1
            yield response.follow(next_page,callback = self.parse)
        
