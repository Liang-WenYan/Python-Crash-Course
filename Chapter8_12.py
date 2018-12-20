def make_sandwiches(*toppings):
    print("\nMaking a sandwich with the follow toppings:")
    for topping in toppings:
        print("- " + topping)


make_sandwiches('pepperoni')
make_sandwiches('mushrooms', 'green peppers', 'extra cheese')
make_sandwiches('extra cheese', 'pepperoni')
