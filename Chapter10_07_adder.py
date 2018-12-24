print("Input two numbers and I'll add them.")
print("(Enter 'q' to quit.)")
active = True

while active:
    first_number = input("\nFirst integer: ")
    if first_number == 'q':
        active = False
    second_number = input("\nSecond integer: ")
    if second_number == 'q':
        active = False
    try:
        adder = int(first_number) + int(second_number)
    except ValueError:
        print("\nSorry.you have to input two integers.")
    else:
        print("The result: " + str(adder))
