from pathlib import Path

import scrapy


class ImobSpider(scrapy.Spider):
    name = "imob"

    def start_requests(self):
        urls = [
            "https://www.storia.ro/ro/oferta/nicolina-biserica-catolica-4-camere-decomandat-3-balcoane-IDsOdz.html",
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
            "Titlu": response.css("h1.efcnut38::text").get(),
            "Pret": response.css("strong.e1l1avn10::text").get(), 
            "Agent": response.xpath("//span[contains(@class, 'e1ckmovd4')]//text()").get(),
            "Agentie": response.xpath("//div[contains(@class, 'e1ckmovd7')]//text()").get(),
            "Adresa": response.css("a.exgq9l20::text").get(),
            "Suprafata utila": response.css("div.enb64yk5::text").get(),
            "Numar de camere": response.css("a.enb64yk0::text").get(),
            "Etaj": response.xpath("//div[contains(@aria-label, 'Etaj')]/div[contains(@class, 'enb64yk2')]/div[contains(@class, 'enb64yk5')]//text()").get(),
        }