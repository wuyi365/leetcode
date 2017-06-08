def bbsort(lst):
    n  =  len(lst)
    for i in range(n, 0, -1):
        for j in range(i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j +1] = lst[j+1], lst[j]

    return lst
ss = [2, 4, 11, 5, 777, 88]
print(bbsort(ss))
