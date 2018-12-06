numbers = list(range(1, 10))
print(numbers)

for number in numbers:
    if number == 1:
        print('\n1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + "th")
