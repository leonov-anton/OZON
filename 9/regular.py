import re

password = input()
resolt = re.match("(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,26}", password)
if resolt:
    print(resolt.group(0))
else:
    print("Неправильный пароль")