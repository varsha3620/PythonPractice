num = [12,34,23,4]
largest = -1
second = -1
for i in num:
    if i > largest:
        second = largest
        largest = i 
    elif i > second:
        second = i
print(second)

# buit in fn
#n = [12,34,23,4]
#n = sorted(set(n))
#print(n[-2])

# sorted :- sorting in ascending order
# set() :- removing duplicate values
