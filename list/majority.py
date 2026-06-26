l = [2, 2, 1, 2, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3]
for i in l:
    count=0
    for j in l:
        if j==i:
            count=count+1
    if count>len(l)//2:
        print(i)
        break