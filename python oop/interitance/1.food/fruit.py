from .food import Food


class Fruit(Food):
    def __init__(self, expiration_date, name: str):
      super().__init__(expiration_date)
      self.name = name

    