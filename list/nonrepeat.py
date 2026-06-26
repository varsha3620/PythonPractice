#first non repeating element

nums = [4, 2, 1, 2, 4, 5, 1, 6]
for i in nums:
    count = 0
    for j in nums:
        if j == i:
            count += 1
    if count == 1:
        print(i)
        break
