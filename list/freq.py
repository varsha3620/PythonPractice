#Frequency of elements
# built in

#nums = [1, 2, 3, 2, 1, 4, 2, 3, 1]
#visited = []
#for i in nums:
 #   if i not in visited:
  #      print(i ,":", nums.count(i))
   #     visited.append(i)

nums = [1, 2, 3, 2, 1, 4, 2, 3, 1]
visited = []
for i in nums:
    if i not in visited:
        count = 0

        for j in nums:
            if i == j:
                count += 1
        print(i, ":", count)
        visited.append(i)