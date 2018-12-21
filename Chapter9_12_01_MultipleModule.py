class User:
    def __init__(self, first_name, last_name, field, age):
        self.first_name = first_name
        self.last_name = last_name
        self.field = field
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("My name is " + self.first_name.title() + self.last_name.title() + " and I am " + str(
            self.age) + " years old."
              + "I am major in " + self.field + "!")

    def greet_user(self):
        print("Hello," + self.first_name.title() + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("\nlogin_attempts at present: " + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("\nset_login_attempts now: " + str(self.login_attempts))
