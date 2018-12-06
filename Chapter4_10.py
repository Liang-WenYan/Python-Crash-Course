my_fools = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream', 'apple', 'banana']
print("The first three items in the list are: ")
for fools in my_fools[:3]:
    print(fools)
c = len(my_fools)
b = c // 2
print("Three items from the middle of the list are: ")
for i in my_fools[b-1:b + 2]:
    print(i)
print("The last three items in the list are: ")
for j in my_fools[-3::]:
    print(j)
