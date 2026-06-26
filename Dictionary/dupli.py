#find duplicates

nums = [1, 3, 4, 2, 2]
duplicates = {}
for i in nums:
   if i in duplicates:
      duplicates[i] += 1
   else:
        duplicates[i] = 1
for key, value in duplicates.items():
    if value > 1:
        print(key)