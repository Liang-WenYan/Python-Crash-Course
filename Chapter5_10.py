current_users = ['admin', 'user1', 'user2', 'user3', 'user4', 'usEr7']
new_users = ['user5', 'user4', 'user7', 'user8', 'USer1']

for new_user in new_users:
    if new_user in current_users:
        print("This user name has been used,please use other name.")
    else:
        print("This user name is available.")

print('\n')
'''
把列表current_users中的全部元素的字母都转为小写字母形式
'''
current_user = []
for current__user in current_users:
    current_user.append(current__user.lower())
print(current_user)

print('\n')

for new_user in new_users:
    if new_user.lower() in current_user:
        print("This user name has been used,please use other name.")
    else:
        print("This user name is available.")
