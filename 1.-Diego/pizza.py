def make_pizza(size, *toppings):
    """Esto es un Doc. String que te dice como funciona la funcion
       valga la redundancia.
    """
    print(f"\nMaking a {size}-in pizza with the followings toppings: ")
    for i in toppings:
        print(f" - {i}")
