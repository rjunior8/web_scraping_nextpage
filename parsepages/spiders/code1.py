# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from lxml import html

from parsepages.items import Links

class Test(CrawlSpider):
	name = "test"
	allowed_domains = ["melhorescola.com.br"]
	start_urls = ["https://www.melhorescola.com.br/escola/busca?municipio=Caruaru&omni=&bairro=&redes=privada&series=&bairros=&sort=&mensalidadeMax=&mensalidadeMin="]
	rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=("//a[contains(@class, 'page-link')]",)), callback="parse_page", follow=True),)

	def parse_page(self, response):
		site = html.fromstring(response.body_as_unicode())
		item = Links()
		for link in site.xpath("//div[contains(@class, 'col-12 col-md6 col-lg-6 card-search-item')]/a[contains(@class, 'card-link')]//@href"):
			item["link"] = link
			yield item
