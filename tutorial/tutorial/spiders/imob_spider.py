from pathlib import Path

import scrapy


class ImobSpider(scrapy.Spider):
    name = "imob"

    def start_requests(self):
        urls = [
            "https://www.imobiliare.ro/vanzare-apartamente/iasi/copou/apartament-de-vanzare-2-camere-XCEQ101LO",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-4]
        filename = f"imob-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")