my_pizzas = ["hawaiian", "spinech and feta", "cheese", "vegetarian"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("pesto")
friend_pizzas.insert(1, "pepperoni")
print("My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
print("The first 3 items of my list are:")
for my_pizza in my_pizzas[:3]:
    print(my_pizza)
print("The first 3 items of my friend's list are:")
for friend_pizza in friend_pizzas[:3 ]:
    print(friend_pizza)