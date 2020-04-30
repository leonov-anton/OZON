def palindrome(s):
    d = s.split()
    c = "".join(d)
    kol_symb = len(c) // 2
    spisok = list(c.lower())
    first_part = spisok[:kol_symb]
    second_part = spisok[kol_symb + len(c) % 2:]
    second_part = second_part[::-1] #не получается развернуть методом .reverse()
    if first_part == second_part:
        a = "Полиндром"
    else:
        a = "Не полиндром"
    print(a)

s = input("Введите текст: ")
palindrome(s)