favorite_languages = {
    'jen': 'python',
    'Sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
}
friends = ['jen', 'yanyan', 'phil', 'binbin']
for name in friends:

    if name in favorite_languages.keys():
        print(name.title() + ",thank you for taking the poll.")
    else:
        print(name.title() + ",please take the poll.")
