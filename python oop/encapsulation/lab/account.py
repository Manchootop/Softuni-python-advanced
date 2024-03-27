class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    @property
    def get_id(self):
        return self.__id

    @get_id.setter
    def get_id(self, value):
        self.__id = value

    @property
    def change_pin(self):
        return self.__pin


    @change_pin.setter
    def change_pin(self, old_pin, new_pin):
        if self.__pin == new_pin:
            print('Wrong pin')
        else:
            self.__pin = new_pin

