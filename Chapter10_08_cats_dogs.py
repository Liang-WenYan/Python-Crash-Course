while True:
    print("Enter 'q' to finish.")
    name = input("Cat's name: " + "\n")
    # print("Enter 'q' to finish.\n")
    if name != 'q':
        with open('Chapter10_cats.txt', 'a') as file_object:
            file_object.write(name + "\n")
    else:
        break

while True:
    print("\nEnter 'q' to finish.")
    name_dog = input("Dog's name: " + "\n")
    # print("(Enter 'q' to quit.)")
    if name_dog != 'q':
        with open('Chapter10_dogs.txt', 'a') as file_dog:
            file_dog.write(name_dog + "\n")
    else:
        break


def pet_name(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry,the file " + filename + " does not exist.")
    else:
        print(contents)


filenames = ['Chapter10_cats.txt', 'Chapter10_dogs.txt']
for file_name in filenames:
    print(file_name)
    pet_name(file_name)
