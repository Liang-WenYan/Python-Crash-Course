import json

file_numbers = 'file_num.json'
try:
    with open(file_numbers) as file_obj:
        numbers = json.load(file_obj)
except FileNotFoundError:
    numbers = input("Input your favorite numbers: ")
    with open(file_numbers, 'w') as f_obj:
        json.dump(numbers, f_obj)
        print("We will remember your favorite numbers.")
else:
    print("I know your favorite numbers!It's " + numbers)
