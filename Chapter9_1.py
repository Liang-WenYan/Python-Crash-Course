class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            "\nThe restaurant named " + self.restaurant_name.title() + " is serves " + self.cuisine_type.title() + "!")

    def open_restaurant(self):
        print("Open!!!")


my_restaurant = Restaurant('YanYan', 'Western-type food')
your_restaurant = Restaurant('binbin', 'Chinese food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print(
    "\nMy restaurant names " + my_restaurant.restaurant_name.title() + ",and we make " + my_restaurant.cuisine_type + "!")
