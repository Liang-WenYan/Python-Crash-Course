number = input("Input a number and I will tell you if it's integral multiple of 10. ")
number = int(number)
if number % 5 == 0:
    print("The number " + str(number) + " is integral multiple of 10.")
else:
    print("The number " + str(number) + " isn't integral multiple of 10.")
