def firmat_name(first, last, otch=''):
    """Правильное форматрирование имени"""
    if otch:
        full_name = f'{first.title()} {last.title()} {otch.title()}'
    else:
        full_name = f'{first.title()} {last.title()}'
    return full_name