from Chapter9_12_01_MultipleModule import User


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
