while True:
    result = input("Why do you love programming? ")
    print("Enter 'q' to finish.")
    if result != 'q':
        with open('Chapter10_poll_result.txt', 'a') as file_object:
            file_object.write(result + "\n")
    else:
        break
