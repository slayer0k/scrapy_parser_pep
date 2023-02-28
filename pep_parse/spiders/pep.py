import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css(
            '#numerical-index a.pep.reference.internal::attr(href)'
        ).extract()
        for pep_link in pep_links[::1]:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(sefl, response):
        number, name = response.css('h1.page-title::text').get().split('–', 1)
        yield {
            'number': number.replace('PEP', '').strip(),
            'name': name.strip(),
            'status': response.css(
                '#pep-content > dl > dt:contains("Status") ~ dd > abbr::text'
            ).get()
        }