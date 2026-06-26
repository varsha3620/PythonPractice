#reverse a number

#built in methods

#nums = [1, 2, 3, 4, 5]
#i = nums[::-1]
#print(i)

#nums = [1, 2, 3, 4, 5]
#nums.reverse()
#print(nums)

#Two pointer method

nums = [1,2,3,4,5]
left = 0
right = len(nums)-1
while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -=1
print(nums)

