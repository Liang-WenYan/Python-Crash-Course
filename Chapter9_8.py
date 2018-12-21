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


class Admin(User):
    def __init__(self, first_name, last_name, field, age):
        super().__init__(first_name, last_name, field, age)
        self.privileges = Privileges(
            ['can add post', 'can delete post', 'can ban post'])  # you need to pass a privileges_admin here!


class Privileges():
    def __init__(self, privileges_admin):
        self.privileges_admin = []
        self.privileges_admin = privileges_admin
        print("BinBin love Yanyan.")

    # ['can add post', 'can delete post', 'can ban post']

    def show_privileges(self):
        for privilege in self.privileges_admin:
            print(privilege)


if __name__ == "__main__":
    wenyan = Admin('wen', 'yan', 'network', 17)
    wenyan.privileges.show_privileges()
