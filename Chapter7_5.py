prompt = "\nInput your age and I will tell you the price:"
prompt += "\nEnter 'quit' to end the program."
while True:
    age = input(prompt)
    age = float(age)
    if age != 'quit':
        if age < 3:
            print("You are free!")
        elif age >= 3 and age <= 12:
            print("You should pay 10 dollar.")
        elif age > 12:
            print("You should pay 15 dollar!")
    else:
        break
