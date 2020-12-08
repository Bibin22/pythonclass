lst = [1, 2, 3, 4]
l = 0
u = len(lst)-1
element = 3
while (l<u):
    total = lst[l] + lst[u]
    if element < total:
        u = u -1
    elif element > total:
        l = l + 1
    elif element == total:
        print("(",lst[l], ",", lst[u], ")")
        break

"""for i in lst:
    for j in lst:
        if i + j == n:
            print(i, j)
            break"""