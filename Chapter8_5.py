def describe_city(city, country='China'):
    print(city.title() + " is in " + country.title() + "!")


describe_city('Reykjavik', 'Iceland')
describe_city('beijing')
describe_city(city='guangzhou')
describe_city(country='seattle', city='America')  # 这个是错误的示例，关键字参数仍然遵循位置参数的顺序。
