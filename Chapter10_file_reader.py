with open('Chapter10_pi.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
# open()函数，打开文件，接受一个参数：要打开的文件的名称。python在当前执行的文件所在的目录中查找指定的文件。
# 关键字with 在不需要访问文件后将其关闭
# read()方法，读取这个文件的全部内容，在python3.5中，read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行，删除末尾空行可使用rstrip()

print("\n绝对文件路径，打开文件")
# Windows系统，文件路径使用的是反斜杆，由于反斜杆在Python中被视为转义标记，为在Windows中确保万无一失，应以原始字符串的方式
# 指定路径，即在开头的单引号前加上r
file_path = r'D:\Codes\Python入门练习文件\《python编程》源代码文件\chapter_10\pi_digits.txt'
with open(file_path) as file_pi:
    pi = file_pi.read()
    print(pi)
