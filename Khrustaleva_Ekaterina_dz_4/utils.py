from datetime import datetime
from decimal import Decimal

from requests import utils, get

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encoding = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encoding)

rates_date = next(s for s in content.split() if s.startswith('Date="'))
rates_date = rates_date.split('"')[1]
rates_date = datetime.strptime(rates_date, '%d.%m.%Y').date()

content = content.replace('</Value>', '').split('</Valute>')


def currency_rates(currency):
    currency = currency.lower()

    for line in content:
        if currency in line.lower():
            line = line.split('>')
            line.reverse()
            result = line[0].replace(',', '.')
            result = Decimal(result)
            return result, rates_date

    return None, rates_date
