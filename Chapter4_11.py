pizza = ['pizza1', 'pizza2', 'pizza3']
for i in pizza:
    print("I love " + i)
print("I really love " + pizza[1])

friend_pizzas = pizza[:]
print(friend_pizzas)
pizza.append('pizza4')
print(pizza)
friend_pizzas.append('pizza5')
print(friend_pizzas)

print("My favorite pizzas are ")
for j in pizza:
    print(j)

print("My favorite pizzas are ")
for k in friend_pizzas:
    print(k)
