favorite_places = {
    'yanyan': ['shenzhen', 'guangzhou'],
    'binbin': ['Seattle', 'Los Angeles', 'shanghai'],
    'banban': ['shenzhen'],
}
for name, place in favorite_places.items():
    if len(place) > 1:
        print(name + "'s favorite places are:")
        for p in place[:]:
            print(p)
    else:
        print(name + "'s favorite place is:")
        for p in place[:]:
            print(p)
