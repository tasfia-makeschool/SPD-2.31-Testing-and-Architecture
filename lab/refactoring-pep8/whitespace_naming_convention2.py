# By Kami Bigdely
# PEP8 - whitespaces and variable names.


class Pizza:
    def __init__(self, bread_type, cheese_type, meat_type, pizza_toppings, size):
        self.bread_type = bread_type
        self.cheese_type = cheese_type
        self.meat_type = meat_type
        self.toppings = pizza_toppings
        self.size = size

    @classmethod
    def create_chicago_pizza(cls, size):
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meat_type = 'italian sausage'
        toppings = ['green bell pepper', 'mushroom', 'chunky tomato sauce',
                    'onion']
        return cls(bread, cheese, meat_type, toppings, size)

    @classmethod
    def create_california_pizza(cls, meat_type, size):
        bread = 'thin crust'
        cheese = 'feta cheese'
        toppings = ['garlic', 'spinach', 'broccoli', 'olives', 'red onion',
                    'red bell pepper']
        return cls(bread, cheese, meat_type, toppings, size)

    def printInfo(self):
        print('bread type is: ', self.bread_type)
        print('cheese type is: ', self.cheese_type)
        print('meat type is: ', self.meatType)
        print('Toppings are: ', end='')
        print(', '.join(map(str, self.toppings)))


my_pizza = Pizza.create_california_pizza('chicken', 'large')
my_pizza.printInfo()
