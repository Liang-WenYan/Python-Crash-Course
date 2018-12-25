import json

favorite_numbers = input("Input your favorite numbers: ")
favorite_num = 'numbers.json'
with open('favorite_num', 'w') as f_obj:
    json.dump(favorite_numbers, f_obj)
    print("We will remember your favorite numbers.")

with open('favorite_num') as file_obj:
    numbers = json.load(file_obj)
    print("I know your favorite numbers!It's " + numbers)
