def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""
    #print(toppings)

    msg = f"\nMaking a {size} - inche pizza with the following topping:"
    if len(toppings) > 1:
        msg = f"\nMaking a {size} - inche pizza with the following toppings:"

    print(msg)
    #print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
