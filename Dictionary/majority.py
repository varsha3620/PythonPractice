# find majority elements

nums = [2, 2, 1, 2, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3]
freq= {}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for key, value in freq.items():
    if value > len(nums)//2:
        print(key)