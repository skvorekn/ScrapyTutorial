import scrapy

class QuoteSpider(scrapy.Spider):
    # expects these two variables
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # method
    # response will be the source code of the start_url
    def parse(self, response):
        # don't return title tag (css condition)
        # css selector
        title = response.css('title::text').extract()
        # shown as a dictionary
        # return keyword usually, we use yield instead because it is usually used with a generator
        # that is used by Scrapy behind the scenes
        yield {'titletext' : title}

# notes
# scrapy shell "websitename"
# selector gadget chrome extension for easier interpretation of HTML/finding selections of same class/ID
# xpath in terminal
# combine css selector and xpath selector to give condition to extract data
# response.css("li.next a").xpath("@href").extract()
