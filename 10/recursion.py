def fuct_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fuct_rec(n-1)


print(fuct_rec(4))