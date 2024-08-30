print("amigos:")
amigos = int(input())

pizza = (amigos / 8)
pizza_validation = pizza

pizza_validation = int(pizza) + (1 if pizza % 1 != 0 else 0)

print("pizza valid",pizza_validation)
print("pizzas:",pizza)