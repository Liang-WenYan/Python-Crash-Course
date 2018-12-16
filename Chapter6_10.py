favorite_number = {
    'binbin': [42, 59, 63],
    'yanyan': [88, 99, 66, 22, 55],
    'xiaohua': [77, 44, 22, 33, 66],
    'xiaoming': [8, 5, 6],
    'xiaohong': [9, 2, 6, 7],
}
for name, number in favorite_number.items():
    print(name + "'s favorite numbers are:")
    for n in number:
        print(n)