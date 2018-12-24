print("Input two numbers,and I'll add them.")
print("(Enter 'q' to quit.)")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond_number: ")
    if second_number == 'q':
        break
    try:
        answer = float(first_number) + float(second_number)
    except ValueError:
        print("Sorry,you have to input two number.")
    else:
        print(answer)
