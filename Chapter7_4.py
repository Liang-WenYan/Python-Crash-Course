'''7.2.2'''
'''
prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
'''
'''7.2.3'''
'''
prompt = "\nTell me something and I will repeat it back to you!"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        print("\nGame over!")
        active = False
'''
prompt = "\nAdd the toppings to the pizza: "
prompt += "\n(Enter 'quit' to finish.)"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("We will add " + topping + " to your pizza.")
    else:
        break
