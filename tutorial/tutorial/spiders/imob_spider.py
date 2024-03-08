from pathlib import Path

import scrapy


class ImobSpider(scrapy.Spider):
    name = "imob"

    def start_requests(self):
        urls = [
            "https://storia.ro/ro/oferta/nicolina-biserica-catolica-4-camere-decomandat-3-balcoane-IDsOdz.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-4]
        filename = f"imob-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")