nums = [0, 1, 0, 3, 12]
result = []
for x in nums:
    if x != 0:
        result.append(x)       #result = [x for x in nums if x! = 0]
zero = len(nums) - len(result)
for i in range(zero):
    result.append(0)
print(result)

#without built in fn

#nums = [0,1,0,3,12]
#pos = 0
#for x in range(len(nums)):
 #   if nums[x]!=0:
  #      nums[pos],nums[x] = nums[x], nums[pos]
#     pos += 1
#print(nums)
