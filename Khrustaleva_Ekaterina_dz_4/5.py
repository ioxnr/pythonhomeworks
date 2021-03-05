from sys import argv

from utils import currency_rates


def main(args):
    currencies = ('USD', 'США', 'EUR', 'Евро')

    if len(args):
        currencies = args

    for currency in currencies:
        rate, rates_date = currency_rates(currency)
        print(f'{rates_date} {rate}')


if __name__ == '__main__':
    main(argv[1:])
