


def apply_discount(product, discount):
    price = int(product['цена'] * (1 - discount))
    assert 0 <= price <= product["цена"]
    return price, product['марка']


car = {'марка': "volvo", 'цена': 2000}

skidka = float(input())
print(apply_discount(car, skidka))
