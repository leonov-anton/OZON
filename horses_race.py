bet_list = {}


def do_bet(horse_num, bet):
    bet_list.setdefault(horse_num, bet)
    return bet_list

# ставки первого игрока
user = input("Введите Ваше имя: ")
user_bats_kol = int(input("Сколько ставок вы хотите сделать: "))
for i in range(user_bats_kol):
    horse_num = int(input("Введите номер лошади, на которую хотите поставить: "))
    bet = int(input("Введите ставку: "))
    if bet > 0:
        do_bet(horse_num, [user, bet])
    else:
        print("Ставка не может быть нулевой, она не принята")

for key, value in bet_list.items():
    print("Лошадь №" + str(key) + " - ставка - " + str(value))

# ставки второго игрока
user = input("Введите Ваше имя: ")
print("Внимание! Ставки на лошадей под номерами ", end = '')
print(*bet_list.keys(), end = '')
print(" уже сделаны и приняты не будут.")
user_bats_kol = int(input("Сколько ставок вы хотите сделать: "))
for i in range(user_bats_kol):
    horse_num = int(input("Введите номер лошади, на которую хотите поставить: "))
    bet = int(input("Введите ставку: "))
    if bet > 0:
        do_bet(horse_num, [user, bet])
    else:
        print("Ставка не может быть нулевой, она не принята")

for key, value in bet_list.items():
    print("Лошадь №" + str(key) + " - ставка - " + str(value))