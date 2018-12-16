'''
aliens = []

for alien_number in range(30):
    new_aliens = {"color": "red", "points": 6, "speed": "slow"}
    aliens.append(new_aliens)
for alien in aliens[:5]:
    print(alien)
print("......")

print("The total number of aliens is " + str(len(aliens)))

'''

'''
修改前三个外星人的属性

aliens = []

for alien_number in range(30):
    new_aliens = {'color': 'red', 'points': 5, 'speed': 'slow'}
    aliens.append(new_aliens)

for alien in aliens[:5]:
    print(alien)
print("......")

print("The total number of aliens is " + str(len(aliens)))

for alien in aliens[:3]:
    if alien['color'] == 'red':
        alien['color'] = 'green'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print("......")
'''

'''chapter6_4'''
dictionary = {
    'python': '这个是python',
    'C': '这个是C',
    'Ruby': '这个是Ruby',
    'Java': '这个是Java',
    'C++': '这个是C++',
}
for language in dictionary.values():
    print(language.title())
print('......')
dictionary = {
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
for language in dictionary.values():
    print(language.title())
