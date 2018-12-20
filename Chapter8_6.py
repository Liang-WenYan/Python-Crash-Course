def city_country(city, country=''):
    return city.title() + ',' + country.title()


print(city_country(city='santiago', country='chile'))
print(city_country(city='seattle', country='America'))
print(city_country(city='beijing'))
