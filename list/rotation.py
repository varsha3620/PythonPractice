#rotate an array 1 time
# built in

#nums = [1,2,3,4,5]
#result = [nums[-1]]+ nums[:-1]
#print(result)

nums = [1,2,3,4,5]
result = []
result.append(nums[len(nums)-1])
for i in range(len(nums)-1):
    result.append(nums[i])
print(result)