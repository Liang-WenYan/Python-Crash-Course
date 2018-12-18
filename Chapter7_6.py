prompt = "\nInput your age and I will tell you the price:"
prompt += "\nEnter 'quit' to end the program."
'''使用break'''
'''
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
'''
'''while循环中使用条件测试来结束程序'''
'''
age = ''
while age != 'quit':
    age = input(prompt)
    if age != 'quit':
        age = float(age)
        if age < 3:
            print("You are free!")
        elif age >= 3 and age <= 12:
            print("You should pay 10 dollar.")
        elif age > 12:
            print("You should pay 15 dollar!")
'''
'''使用变量active来控制循环结束的时机'''
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = float(age)
        if age < 3:
            print("You are free!")
        elif 3 <= age <= 12:
            print("You should pay 10 dollar.")
        elif age > 12:
            print("You should pay 15 dollar!")
