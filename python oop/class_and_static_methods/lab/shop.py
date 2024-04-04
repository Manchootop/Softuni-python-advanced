class Shop:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, capacity=10)

    def add_item(self, item_name):
        if len(self.items) >= self.capacity:
            return "Not enough capacity in the shop"
        else:
            self.items[item_name] = self.items.get(item_name, 0) + 1
            return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        else:
            self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the shop"

        
