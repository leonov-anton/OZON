import re

text = input()
# проверка на почту
result = re.match(r'^[\a-zA-Z0-9_\.\-]+@\w+\.\w+$', text)
if result:
    print(result.group(0))
else:
    print("Вы вводите какую-то дичь")
# проверка на телефон
# +7 123 1234567
result = re.match(r'(\+7|8|7)( |)\d{3}( |)\d{7}', text)
if result:
    print(result.group(0))
else:
    print("Вы вводите какую-то дичь")