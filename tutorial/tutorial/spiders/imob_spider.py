from pathlib import Path

import scrapy
import json


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

        agent_details = response.xpath("//script[contains(@id, '__NEXT_DATA__')]//text()")
        yield {
            "Titlu": response.css("h1.efcnut38::text").get(),
            "Pret": response.css("strong.e1l1avn10::text").get(), 
            #"Agent": response.xpath("//span[contains(@class, 'e1ckmovd4')]//text()").get(),
            "Agent": response.xpath("/html/body/script[3]//text()").re(r"contactDetails"),
            "Agentie": response.xpath("/div/div[contains(@class, 'ehfvn5x1')]/div[contains(@class, 'e11fbx770')]/strong[contains(@aria-label, 'Numele agenției')]//text()").get(),
            "Agentie": response.xpath("//p[contains(@class, 'e1vciwah5')]//text()").get(),
            "Adresa": response.css("a.exgq9l20::text").get(),
            "Suprafata utila": response.css("div.enb64yk5::text").get(),
            "Numar de camere": response.css("a.enb64yk0::text").get(),
            "Etaj": response.xpath("//div[contains(@aria-label, 'Etaj')]/div[contains(@class, 'enb64yk2')]/div[contains(@class, 'enb64yk5')]//text()").get(),
        }