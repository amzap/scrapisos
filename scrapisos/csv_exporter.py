from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter

FIELDS_TO_EXPORT = [
        'title',
        'price',
        'm2',
        'rooms',
        'planta',
        'ascensor',
        'comentarios',
        'link'
        ]

class MyCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['fields_to_export'] = FIELDS_TO_EXPORT
        super(MyCsvItemExporter, self).__init__(*args, **kwargs)
