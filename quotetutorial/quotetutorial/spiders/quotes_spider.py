import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    # expects these two variables
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # method
    # response will be the source code of the start_url
    def parse(self, response):

        # instance variable
        items = QuotetutorialItem()

        # don't return title tag (css condition)
        # css selector
        # title = response.css('title::text').extract()
        # shown as a dictionary
        # return keyword usually, we use yield instead because it is usually used with a generator
        # that is used by Scrapy behind the scenes
        # yield {'titletext' : title}

        # just extract the first element
        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:

            # don't do extract because want inside the class
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items


# notes
# scrapy shell "websitename"
# selector gadget chrome extension for easier interpretation of HTML/finding selections of same class/ID
# xpath in terminal
# combine css selector and xpath selector to give condition to extract data
# response.css("li.next a").xpath("@href").extract()

# video 11: put into items/containers rather than a database directly
# issue with database:
# issue with dictionaries: lacks structure so move to temporary location (container/items) then to database
# use items.py

# scrapy crawl quotes -o items.json
