#question 1
# Create a class called cart that retains items and has methods to add, remove, and show
from IPython.display import clear_output

class Cart():
    
    '''
        The Cart class will be able to add, remove, and show items.
        
        Expected attributes for the class:
        - items: list of strings
    '''
    
    def __init__(self, items):
        self.items = items
        
    def addItems(self):
        products = input("What would you like to add? ")
        self.items.append(products)
        print(f'{products} has been added to your cart.')
    
    def removeItems(self):
        print("This is what's in your cart")
        for i in self.items:
            print(i)
        remove_product = input("What would you like to remove? ")
        
        try:
            self.items.remove(remove_product)
            print(f"{remove_product} has been removed.")
        except:
            print(f"{remove_product} isn't in your cart! Try again.")
            
    def showItems(self):
        print("Here's what's in your cart:")
        for i in self.items:
            print(i)
            
            
shoppingCart = Cart([])
    
def run():
    while True:
        response = input("What would you like to do? add/remove/show/quit ")
        clear_output()
        
        if response.lower() == 'quit':
            shoppingCart.showItems()
            break
            
        elif response.lower() == 'add':
            shoppingCart.addItems()
            
        elif response.lower() == 'remove':
            shoppingCart.removeItems()
            
        elif response.lower() == 'show':
            shoppingCart.showItems()
            
        else:
            print("Please try something else")

run()
     




#question 2
class Word():
    
    def __init__(self):
        self.string = ""
        pass
    
    def get_String(self):
        self.string = input("Give me a word! : ")
        return self.string

    def print_Caps(self):
        print(self.string.upper())

first_word = Word()
first_word.get_String()
first_word.print_Caps()

second_word = Word()
second_word.get_String()
second_word.print_Caps()