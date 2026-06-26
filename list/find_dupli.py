# Find Duplicate Element

#nums = [1, 3, 3, 4, 2, 2]

#seen = set()
#duplicates = []

#for num in nums:
 #   if num in seen:
  #      if num not in duplicates:
   #         duplicates.append(num) append only use in list 
    #else:
     #   seen.add(num)   add only using in set 

#print(duplicates)

nums = [1, 3, 4, 2, 2]

seen = set()  

for num in nums:
    if num in seen:
        print(num)
        break
    seen.add(num)