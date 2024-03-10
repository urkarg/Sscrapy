from pathlib import Path

import scrapy


class ImobSpider(scrapy.Spider):
    name = "imob"

    def start_requests(self):
        urls = [
            "https://storia.ro/ro/oferta/vanzare-apartament-2-camere-podu-ros-aproape-de-sensul-giratoriu-IDzvZo",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    """ 
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"imob-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
    """
    def parse(self, response):
        yield {
            "Titlu": response.css("h1.efcnut38::text").get()
        }