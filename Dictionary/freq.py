# Frequency of elements
#built in

#nums = [1, 2, 3, 2, 1, 4, 2, 3, 1]
#freq = {}
#for i in nums:
 #   freq[i] = nums.count(i)
#print(freq)


nums = [1, 2, 3, 2, 1, 4, 2, 3, 1]
freq = {}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for key, value in freq.items():
    print(key, ":", value)