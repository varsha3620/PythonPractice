#Find missing number

# without built in fn

#nums = [11, 12, 13, 15]
#start = min(nums)
#end = max(nums)
#expected = 0
#for num in range(start,end+1):
 #   expected += num
#actual = 0
#for i in nums:
 #   actual+=i
#print(expected - actual)

# built in
nums = [11, 12, 13, 15]
expected = sum(range(min(nums),max(nums)+1))
actual = sum(nums)
print(expected - actual)