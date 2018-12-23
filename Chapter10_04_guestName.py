active = True
while active:
    guest_name = input("Input your name: ")
    print("(Enter 'q' to finish.)")
    if guest_name != 'q':
        print("Hello," + guest_name + " nice to meet you!")
        with open('Chapter10_guest_book.txt', 'a') as file_object:
            file_object.write(guest_name + "\n")
    else:
        print("finish input!")
        active = False
