def apply_discount(product, discount):
    dis_price = []
    for i, j in zip(product.values(), discount):
        price = int(i * (1 - j))
        # assert 0 <= price <= product[value]
        dis_price.append(price)
        # return price, product[key]
        print(dis_price)
    # return price, product[key]


data = open('data.txt', 'r', encoding='utf-8')
discount = open('discount.txt', 'r', encoding='utf-8')

price_list = {}
for line in data:
    key, value = line.split(', ')
    value = int(value)
    price_list[key] = value
print(price_list)

discount_list = [float(i) for i in discount]
print(discount_list)

print(apply_discount(price_list, discount_list))


