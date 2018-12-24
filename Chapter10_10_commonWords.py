def count_word(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry the file " + filename + " does not exist.")
    else:
        word = 'the'
        word_number = contents.lower().count(word)
        print("The word 'the' sum: " + str(word_number))


file_path = r'D:\Codes\51804.txt'
file_path2 = 'D:\Codes\\nonono.txt'  # 注意转义字符，文件名与\n,\a,\t,\f之类的转义字符相撞时，文件名要做转义处理，如\\n
count_word(file_path)

