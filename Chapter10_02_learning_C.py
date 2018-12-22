with open('Chapter10_learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.replace('Python', 'C'))
