from typing import List

sandwich_orders = ['tuna', 'ham', 'chicken', 'beef']
finished_sandwiches = []
while sandwich_orders:  # sandwich_orders != []
    sandwich_order = sandwich_orders.pop()
    print("I made your " + sandwich_order + " sandwich.")
    finished_sandwiches.append(sandwich_order)

print("\nThe following sandwiches have been finished:")
for sandwich in finished_sandwiches:
    print(sandwich)
