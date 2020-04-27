# сегодня мы с вами попробуем выступить в роли детектива
# у нас есть множество людей, которые пользуется машинной марки, которую пользуется убийца
# есть множество людей, которые живут недалеко от мест преступления
# и множество людей, у которых и работа недалеко от мест преступления

# имена обычно значения неуникальные, но предплоложим, это были бы номер соц страховок
shevrole_owner = {'sam', 'edit', 'semen', 'petr'}

work_near = {'konstantin', 'vladislav', 'sam', 'petr', 'edit'}

live_near = {'john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo'}

print("СПОСОБ 1. (подсмотрел в интеренет такую возможность, если честно)")
print("Живет рядом, работает рядом и имеет Шевроле: ", end = '')
print(*shevrole_owner & work_near & live_near)
print("Живет рядом и имеет Шевроле: ", end = '')
print(*shevrole_owner & live_near)
print("Живет рядом и работает рядом: ", end = '')
print(*work_near & live_near)
print("Работает рядом и имеет Шевроле: ", end = '')
print(*shevrole_owner & work_near)
print("")

shevrole_owner = list(shevrole_owner)
work_near = list(work_near)
live_near = list(live_near)
full_list = list(set(shevrole_owner + work_near + live_near))

print("СПОСОБ 2:")

a = 0
for i in shevrole_owner:
    for j in live_near:
        for q in full_list:
            if i == j == q:
                print(i + " - владеет шевроле и живет и рабоатет рядом")
                a += 1
else:
    if a == 0:
        print("Никто не живет и не работает рядом, а так же не владеет Шевроле одновременно")
a = 0
for i in shevrole_owner:
    for j in live_near:
        if i == j:
            print(i + " - владеет Шевроле и живет рядом")
            a += 1
else:
    if a == 0:
        print("Никто не живет рядом, а так же не владеет Шевроле одновременно")
a = 0
for i in shevrole_owner:
    for j in work_near:
        if i == j:
            print(i + " - владеет Шевроле и живет рядом")
            a += 1
else:
    if a == 0:
        print("Никто не работает рядом, а так же не владеет Шевроле одновременно")
a = 0
for i in live_near:
    for j in work_near:
        if i == j:
            print(i + " - владеет Шевроле и живет рядом")
            a += 1
else:
    if a == 0:
        print("Никто не живет и не работает рядом одновременно")
print("")
print("СПОСОБ 3:")

for i in full_list:
    if i in work_near and i in shevrole_owner and i in live_near:
        print(i + " - живет рядом, работает рядом и имеет Шевроле")
    elif i in work_near and i in shevrole_owner:
        print(i + " - работает рядом и имеет Шевроле")
    elif i in live_near and i in shevrole_owner:
        print(i + " - живет рядом и имеет Шевроле")
    elif i in live_near and i in work_near:
        print(i + " - живет и работает рядом")
