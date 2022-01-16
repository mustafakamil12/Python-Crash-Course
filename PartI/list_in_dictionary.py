pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese'],
}

for key,value in pizza.items():
    print(key,value)

for topping in pizza['toppings']:
    print(topping)
