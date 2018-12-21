from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['Ruby'] = '这个是Ruby'
favorite_languages['python'] = '这个是python'
favorite_languages['C'] = '这个是C'

favorite_languages['Java'] = '这个是Java'
favorite_languages['C++'] = '这个是C++'
favorite_languages['HTML'] = '这个是HTML'
favorite_languages['CSS'] = '这个是CSS'
favorite_languages['JS'] = '这个是JS'
favorite_languages['PHP'] = '这个是PHP'
favorite_languages['C++'] = '是C++'
print(favorite_languages.items())
for language, describe in favorite_languages.items():
    print(language + " is " + describe)

print("I love Yanyan")
# dict() 3.6 开始是有序的，之前是无序的
favorite_languages_dict = {
    'python': '这个是python',
    'C': '这个是C',
    'Ruby': '这个是Ruby',
    'Java': '这个是Java',
    'C++': '这个是C++',
    'HTML': '这个是HTML',
    'CSS': '这个是CSS',
    'JS': '这个是JS',
    'PHP': '这个是PHP',
    'C++': '这个是C++',
}
# favorite_languages_dict['python'] = '这个是python'
# favorite_languages_dict['C'] = '这个是C'
# favorite_languages_dict['Ruby'] = '这个是Ruby'
# favorite_languages_dict['Java'] = '这个是Java'
# favorite_languages_dict['C++'] = '这个是C++'
# favorite_languages_dict['HTML'] = '这个是HTML'
# favorite_languages_dict['CSS'] = '这个是CSS'
# favorite_languages_dict['JS'] = '这个是JS'
# favorite_languages_dict['PHP'] = '这个是PHP'
# favorite_languages_dict['C++'] = '是C++'
print(favorite_languages_dict.keys())
print(favorite_languages_dict.values())
print(favorite_languages_dict.items())
for language, describe in favorite_languages_dict.items():
    print(language + " is " + describe)