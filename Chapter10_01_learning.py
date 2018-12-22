# 打开整个文件
print("打开整个文件")
with open('Chapter10_learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 打印时遍历文件对象
print("打印时遍历文件对象")
filename = 'Chapter10_learning_python.txt'
with open(filename) as file_object01:
    for line in file_object01:
        print(line)

# 打印时将各行存储在一个列表中，再在with代码块外打印它们
print("打印时将各行存储在一个列表中，再在with代码块外打印它们")
f = 'Chapter10_learning_python.txt'
with open(f) as file_object02:
    lines = file_object02.readlines()
for line in lines:
    print(line.strip())
