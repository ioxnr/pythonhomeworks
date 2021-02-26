products = [57.8, 46.51, 97, 103, 65.33, 40, 67, 5, 23.45, 31, 46, 78.4, 53, 90.3, 26]

for i in products:
    rub = int(i)
    kop = int(100 * (i - rub))
    if rub < 10:
        rub = str(rub).zfill(2)
    if kop < 10:
        kop = str(kop).zfill(2)
    print(f'{rub} руб {kop} коп')

print(id(products))
products.sort()
print(products)
print(id(products))

reversed_products = sorted(products, reverse=True)
print(reversed_products)

most_expensive = reversed_products[0:5]
print(most_expensive)
most_expensive.sort()
print(most_expensive)
