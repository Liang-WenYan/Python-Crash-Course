class User:
    def __init__(self, first_name, last_name, field, age):
        self.first_name = first_name
        self.last_name = last_name
        self.field = field
        self.age = age

    def describe_user(self):
        print("My name is " + self.first_name.title() + self.last_name.title() + " and I am " + str(
            self.age) + " years old."
              + "I am major in " + self.field + "!")

    def greet_user(self):
        print("Hello," + self.first_name.title() + self.last_name.title())


wenyan = User('wen', 'yan', 'network', 17)
yibin = User('yi', 'bin', 'electronic', 18)
yuban = User('yu', 'ban', 'math', 1)
wenyan.describe_user()
wenyan.greet_user()
yibin.describe_user()
yibin.greet_user()
yuban.describe_user()
yuban.greet_user()
