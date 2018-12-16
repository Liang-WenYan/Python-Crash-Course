rivers = {
    'nile': 'egypt',
    'Changjiang': 'China',
    'Yellow River': 'China',
}
for river, country in rivers.items():
    print("\nthe " + river + " runs through " + country.title())
for river in rivers.keys():
    print('\n' + river)
for country in rivers.values():
    print('\n' + country.title())
