binbin = {
    'firstname': 'zeng',
    'lastname': 'yibin',
    'age': 22,
    'city': 'GuangZhou',
}
yanyan = {
    'firstname': 'liang',
    'lastname': 'wenyan',
    'age': 23,
    'city': 'guangzhou',
}
banban = {
    'firstname': 'liang',
    'lastname': 'yuban',
    'age': 1,
    'city': 'shenzhen',
}

peoples = [binbin, yanyan, banban]

for people in peoples[:]:
    print(people)
