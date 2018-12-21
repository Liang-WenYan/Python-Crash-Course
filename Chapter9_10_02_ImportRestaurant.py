from Chapter9_10_01_ImportRestaurant import Restaurant

# 如果 import 一个模块，那么模块__name__ 的值通常为模块文件名，不带路径或者文件扩展名。
print("02 __name__ : %s" % __name__)

yy_restaurant = Restaurant('yy', 'Chinese food')
yy_restaurant.describe_restaurant()