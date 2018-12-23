name = input("Input your name: ")

with open('Chapter10_guest.txt', 'a') as file_object:
    file_object.write(name + "\n")
