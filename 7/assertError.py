def apply_discount(product, discount):
    price = int(product['цена']*(1-discount))
    assert 0 <= price <= product['цена']
    return price, product['марка']


car = {'марка': "volvo", 'цена': 2000}

print(apply_discount(car, 0.25))

print(apply_discount(car, 1.25))