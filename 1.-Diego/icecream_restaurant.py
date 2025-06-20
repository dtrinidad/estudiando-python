from restaurant import Users
from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Una heladeria"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Constructor que hereda de padre"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def describe_flavors(self):
        print("Our list of flavors is:")
        for i in self.flavors:
            print(f" - {i.title()}")
class Privilege:
    """una clase separade de privilegio para luego pasarle a admin user"""
    def __init__(self, list_privilege = ["add_post", "del_post", "ban_user"]):
        self.list_privilege = list_privilege
    
    def show_privilege(self):
        print("Privilege: ")
        for i in self.list_privilege:
            print(f" * {i.title()}")

class Admin(Users):
    """Administrador"""
    def __init__(self, first_name, last_name):
        """construyendo al admin del grupo"""
        super().__init__(first_name, last_name)
        self.privilege = Privilege()




list_of_flavors = ["Strawberry", "pinaple", "Mango", "macadamia", "granada"]
my_heladeria = IceCreamStand("Diego's ICE", "Heladeria", list_of_flavors )
my_heladeria.describe_flavors()


my_admin = Admin("Marcus", "Trinidad")
my_admin.privilege.show_privilege()