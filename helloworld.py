arr =[1, 2, 3, 4, 5]
n = 4
l = 0
u = len(arr)-1
while l <= u:
    mid = (l + u) // 2
    if arr[mid] == n:
        p = mid
        print(n, "found at position", p)
        break
    elif arr[mid] < n :
        l = mid + 1
    elif arr[mid] > n :
        u = mid - 1
else:
    print("item not found")