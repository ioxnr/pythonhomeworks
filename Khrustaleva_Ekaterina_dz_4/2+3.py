from datetime import datetime
from decimal import Decimal

from requests import utils, get

API_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates_date(content):
    rates_date = next(s for s in content.split() if s.startswith('Date="'))
    rates_date = rates_date.split('"')[1]
    return datetime.strptime(rates_date, '%d.%m.%Y').date()


def currency_rates(currency):
    response = get(API_URL)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    print(currency_rates_date(content))

    content = content.replace('</Value>', '').split('</Valute>')
    currency = currency.lower()
    for line in content:
        if currency in line.lower():
            line = line.split('>')
            line.reverse()
            result = line[0].replace(',', '.')
            result = Decimal(result)
            return result

    return None


print(currency_rates('EUR'))
print(currency_rates('RUB'))
print(currency_rates('Сингапурский доллар'))
print(currency_rates('INR'))
print(currency_rates('Норвежских крон'))
print(currency_rates('USD'))
print(currency_rates('доллар сша'))
print(currency_rates('евро'))
