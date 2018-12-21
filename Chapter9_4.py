class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 10

    def describe_restaurant(self):
        print(
            "\nThe restaurant named " + self.restaurant_name.title() + " is serves " + self.cuisine_type.title() + "!")

    def open_restaurant(self):
        print("Open!!!")

    def restaurant(self):
        print("\nHow many people have been served at this restaurant? : " + str(self.number_served))

    def set_number_served(self, served):
        self.number_served = served
        print("\nHow many people at this time? : " + str(self.number_served))

    def increment_number_served(self, increment_served):
        self.number_served += increment_served
        print("\nHow many people would be served at this restaurant every day? : " + str(self.number_served))


my_restaurant = Restaurant('YanYan', 'Western-type food')
my_restaurant.restaurant()
my_restaurant.set_number_served(20)
my_restaurant.increment_number_served(25)
