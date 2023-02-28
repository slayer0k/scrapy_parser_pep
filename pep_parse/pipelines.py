import csv
import datetime as dt

from pep_parse.settings import FILE_PATH, BASE_DIR


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
            writer = csv.DictWriter(
                file, fieldnames=fieldnames, lineterminator='\n'
            )
            writer.writeheader()
            for key, value in self.statuses.items():
                writer.writerow({'Статус': key, 'Количество': value})
            writer.writerow({
                'Статус': 'Total',
                'Количество': sum(self.statuses.values())
            })
