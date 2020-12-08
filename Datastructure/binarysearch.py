lst = [1, 2, 3, 4, 5, 6]
l = 0
u = len(lst)-1


n = int(input("Enter a number to search"))
while l <= u:
    mid = (l + u) // 2
    if lst[mid] == n:
        p = mid
        print(n, "found ", p)
        break

    elif lst[mid] > n:
        u  = mid - 1
    elif lst[mid] < n:
        l = mid + 1

else:
    print("not found")
