class Chef:

    def make_chicken(self):
        print("the chef can make chicken")

    def make_salad(self):
        print("the chef can make salad")

    def make_special(self):
        print("the chef can make special ribs")

# class that inherits above claass
'''from chef import Chef

class ChineseChef(Chef):

    def make_special(self):
        print("the chef can make orange chicken")

    def make_fried_rice(self):
        print("the chef can make fried rice")'''
# Code to check what the chef can make
'''from chef import Chef
from chinesechef import ChineseChef

mychef = Chef()
mychef.make_special()

mychinesechef = ChineseChef()
mychinesechef.make_special()'''