#first non repeating element

nums = [4, 2, 1, 2, 4, 5, 1, 6]
freq = {}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for i in nums:
    if freq[i] == 1:
        print(i)
        break
