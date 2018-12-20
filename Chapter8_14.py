def make_car(manufacturer, types, **other_info):
    car = {}
    car['manufacturer_name'] = manufacturer
    car['type_name'] = types
    for key, value in other_info.items():
        car[key] = value
    return car


print(make_car('subaru', 'outback', color='blue', tow_package=True))
print(make_car('yanyan', 'binbin', color='red'))
