def make_pizza(size, *toppings):
    "Apresenta a pizza que estamos prestes a preparar"
    print("\Making a" + str(size) + "-inch pizza whith the following toppings")
    for topping in toppings:
        print("- " + topping)