import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from ..items import ScraperHw6Item
from urllib.parse import urljoin


class BooksSpiderSpider(CrawlSpider):
    name = "books_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//article[@class='product_pod']")), callback="parse_item", follow=True),
        # Rule(LinkExtractor(restrict_xpaths=("//li[@class='next']"))), #для пагинации
        )

    def parse_item(self, response):
        # print(response.url)
        loader = ItemLoader(item=ScraperHw6Item(), response=response)
        loader.default_input_processor = MapCompose(str.strip)

        loader.add_xpath("book_name", "//h1/text()")
        loader.add_xpath("book_price", "//tr[4]/td/text()")
        loader.add_xpath("book_available", "//tr[6]/td/text()")

        half_image_link = response.xpath("//div[@class='item active']/img/@src").getall()
        image_link = [urljoin("https://books.toscrape.com", img_url) for img_url in half_image_link]

        loader.add_value("image_urls", image_link)
        
        # loader.add_xpath("image_urls", "//div[@class='item active']/img/@src")

        yield loader.load_item()
