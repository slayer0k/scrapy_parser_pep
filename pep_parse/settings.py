from pathlib import Path

BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
ROBOTSTXT_OBEY = True
BASE_DIR = Path(__file__).parent.parent
DOMAIN_URL = 'peps.python.org'
FILE_PATH = 'results'
FEED_EXPORT_ENCODING = 'utf-8'
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
FEEDS = {
    f'{FILE_PATH}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
    }
}
