'''
name: str - if the name is an empty string, raise a ValueError with the message "The name cannot be an empty string"
dough: Dough - if the dough is None, raise a ValueError with the message "You should add dough to the pizza"
toppings_capacity: int – represents the maximum number of toppings the pizza should have.
 If the capacity is 0 or less, raise a ValueError with the message "The topping's capacity cannot be less or equal
  to zero"
toppings: dict – empty dictionary upon initialization that will contain the topping type as a key and the topping's
 weight as a value.

'''
from .dough import Dough
from .topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: dict):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('The name cannot be an empty string')
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError('You should add dough to the pizza')
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value < 0:
            raise ValueError('The topping\'s capacity cannot be less or equal to zero')
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if self.toppings_capacity == 0:
                raise ValueError('The topping\'s capacity cannot be less or equal to zero')
        if topping not in self.toppings:
            self.toppings[topping] = topping.weight
        self.toppings[topping] += topping.weight
        self.toppings_capacity -= 1

    def calculate_total_weight(self):
        total_weight = 0

        total_weight += sum(topping for topping in self.toppings.values())

        total_weight += self.dough.weight

        return total_weight


