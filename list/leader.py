# leader of an array

nums =  [16, 17, 4, 3, 5, 2]
for i in range(len(nums)):
    leader = True
    for j in range(i+1, len(nums)):
        if nums[j]>nums[i]:
            leader = False
            break
    if leader:
        print(nums[i])