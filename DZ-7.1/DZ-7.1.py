import random


def apply_discount(product, discount):
    price = int(product['цена'] * (1 - discount))
    assert 0 <= price <= product['цена']
    return price, product['товар']


data = open('data.txt', 'r', encoding='utf-8')
discount = open('discount.txt', 'r', encoding='utf-8')

# price_list = []
# for line in data:
#     a, b = line.split(', ')
#     price_1 = dict([('товар', a), ('цена', int(b))])
#     price_list.append(price_1)
# print(price_list)

# discount_list = [float(i) for i in discount]
# print(discount_list)

file_name = ''
for i in range(7):
    file_name += random.choice('abcdefghijklmnopqrstuvwxyz')

new_price = open(file_name+'.txt', 'a', encoding='utf-8')

for line, i in zip(data, discount):
    a, b = line.split(', ')
    try:
        new_price.write(str(apply_discount({'товар': a, 'цена': int(b)}, float(i)))+'\n')
    except AssertionError:
        # print("Слишком большая скидка для " + price['товар'].upper())
        new_price.write("Слишком большая скидка для " + a.upper()+'\n')

new_price.close()
data.close()
discount.close()