import csv
import datetime as dt

from pep_parse.settings import BASE_DIR, FILE_PATH


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = {}

    def process_item(self, item, spider):
        self.statuses.setdefault(item['status'], 0)
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        date = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open(
            f'{BASE_DIR / FILE_PATH}/status_summary_{date}.csv',
            'w', encoding='utf-8'
        ) as file:
            fieldnames = ['Статус', 'Количество']
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows([
                fieldnames, *self.statuses.items(),
                ('Всего', sum(self.statuses.values()))
            ])
