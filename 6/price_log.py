import parse
from decimal import Decimal

class PriceLog:

    def __init__(self, location, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price
        self.location = location


    @classmethod
    def parse(cls, location, text_log):

        def price(string):
            return Decimal(string)

        FORMAT = ('[{timestamp}] - SPRZEDAŻ - PRODUKT: {product:d} - '
                  'CENA: {price:price}')
        formats = {'price': price}
        result = parse.parse(FORMAT, text_log, formats)

        return cls(location=location, timestamp=result['timestamp'],
                   product_id=result['product'], price=result['price'])

    @classmethod
    def header(cls):
        return ['LOKALIZACJA', 'CZAS', 'PRODUKT', 'CENA']

    def row(self):
        return [self.location, self.timestamp, self.product_id, self.price]