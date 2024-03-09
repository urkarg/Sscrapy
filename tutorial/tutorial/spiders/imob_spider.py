from pathlib import Path

import scrapy


class ImobSpider(scrapy.Spider):
    name = "imob"

    def start_requests(self):
        urls = [
            "https://storia.ro/ro/oferta/vanzare-apartament-2-camere-podu-ros-aproape-de-sensul-giratoriu-IDzvZo",
            "https://storia.ro/ro/rezultate/vanzare/apartament/iasi?limit=36&ownerTypeSingleSelect=ALL&daysSinceCreated=1&by=DEFAULT&direction=DESC&viewType=listing",
            "https://storia.ro/ro/companii/agentii/top-imobil-ID3949079",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"imob-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")