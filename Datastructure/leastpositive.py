lst = [-2, -1, 0,  2, 3, 4]
#print(1 in lst)
cnt = 1
for i in range(0, len(lst)):
    if cnt in lst:
        cnt +=1
    else:
        print(cnt, "is missing least positive intiger")
        break