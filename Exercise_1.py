#Exercise 1 - Turn the shopping cart program from last week into an object-oriented program
#The comments in the cell below are there as a guide for thinking about the problem. 
#However, if you feel a different way is best for you and your own thought process, 
#please do what feels best for you by all means.


# Create a class called cart that retains items and has methods to add, remove, and show
class ShoppingCart():
    def __init__(self):
        self.cart = {}  
    def add_Item(self):
        item = input("What would you like to add?")
        quantity = input("And how many will you need? ")
        self.cart[item.title()] = quantity
    def show_Items(self):
        print(self.cart)
    def remove_Items(self):
        deletion = input("What would you like to delete?")
        if self.cart.get(deletion.title()):
            del self.cart[deletion.title()]
        else:
            print("I'm sorry, that isn't on your list.")
    def change_Item_Quantity(self):
        item_change = input("What item would you like to change the quantity of? ")
        if self.cart.get(item_change.title()):
            num_change = input("How many do you need? ")
            self.cart[item_change.title()] = num_change
        else:
            print("I'm sorry, that isn't on your list.")


def exercise_1():
    my_list = ShoppingCart()
    while True:
        select = input("Do you want to: Show/Add/Remove/Change Amount or Quit? ").lower()
        match select:
            case "show":
                my_list.show_Items()
            case "add":
                my_list.add_Item()
            case "remove":
                my_list.remove_Items()
            case "change amount":
                my_list.change_Item_Quantity()
            case "quit":
                my_list.show_Items()
                print("Goodbye!")
                break
            case _:
                print("I'm sorry, that isn't one of the options.")
exercise_1()

