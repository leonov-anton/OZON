def fuct_hrec(n):
    return fuct_iter(1,1,n)


def fuct_iter(prod, counter, n):
    if counter > n:
        return prod
    else:
        return fuct_iter(counter*prod, counter+1, n)


print(fuct_hrec(4))