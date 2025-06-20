import pizza
from pizza import make_pizza
import pizza as piz
from pizza import make_pizza as haciendo_pizza


pizza.make_pizza(16, "peperoni")
make_pizza(16, "peperoni", "pinaple", "extra_Cheese")


piz.make_pizza(8,  "peperoni", "rise", "chiken", "pinaple", "extra_Cheese")
haciendo_pizza(12, "rise", "chiken", "pinaple", "extra_Cheese")