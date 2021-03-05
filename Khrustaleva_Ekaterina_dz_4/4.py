from utils import currency_rates

currencies = ('USD', 'США', 'EUR', 'Евро')

for currency in currencies:
    rate, rates_date = currency_rates(currency)
    print(f'{rates_date} {rate}')
