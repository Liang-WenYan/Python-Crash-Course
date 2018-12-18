sandwich_orders = ['pastrami', 'tuna', 'ham', 'pastrami', 'pastrami', 'chicken', 'beef']
print(sandwich_orders)
print("The pastrami have sold out!!!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)