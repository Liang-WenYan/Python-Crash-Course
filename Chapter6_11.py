cities = {
    'guangzhou': {
        'country': 'China',
        'population': '666w',
        'fact': 'I like it.'
    },
    'shenzhen': {
        'country': 'China',
        'population': '766w',
        'fact': 'I like it,too.'
    },
    'Seattle': {
        'country': 'America',
        'population': '686w',
        'fact': 'Binbin like it.'
    },
}
for cityname, city_info in cities.items():
    print("City name:" + cityname)
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(country)
    print(population)
    print(fact)
