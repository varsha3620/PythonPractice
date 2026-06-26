n = 121
original = n
reverse = 0
while n > 0:
    digit = n%10  #we take the remainder that is 1
    reverse = reverse * 10 + digit
    n = n//10
if original == reverse:
    print("pallindrome")
else:
    print("not pallindrome")