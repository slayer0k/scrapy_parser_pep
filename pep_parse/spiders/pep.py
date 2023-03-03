import scrapy

ALLOWED_DOMAINS = ['peps.python.org']


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css(
            '#numerical-index tr td:nth-child(2) a::attr(href)'
        ).extract()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(sefl, response):
        number, name = response.css(
            'h1.page-title::text'
        ).get().split('–', 1)
        yield {
            'number': number.replace('PEP', '').strip(),
            'name': name.strip(),
            'status': response.css(
                '#pep-content > dl > dt:contains("Status") ~ dd > abbr::text'
            ).get()
        }
