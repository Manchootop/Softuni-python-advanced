class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.__name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return 'Not enough budget'

        if len(self.animals) == self.__animal_capacity:
            return 'Not enough space for animal'

        self.animals.append(animal)
        self.__budget -= price

        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if len(self.workers) == self.__worker_capacity:
            return 'Not enough space for worker'

        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired'

    def fire_worker(self, worker_name):
        if worker_name not in self.workers:
            return f'The is no {worker_name} in the zoo'

        self.workers.remove(worker_name)
        return f'"{worker_name} fired successfully'

    def pay_workers(self):
        price_to_pay = sum(worker.salary for worker in self.workers)
        if self.__budget >= price_to_pay:
            self.__budget -= price_to_pay
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        price_to_tend = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= price_to_tend:
            self.__budget -= price_to_tend
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    # def animals_status(self):
    #     # get animals_count
    #     total_animals_count = len(self.animals)
    #
    #     # split them into types
    #     animals_by_type = {}
    #     for animal in self.animals:
    #         animal_type = type(animal).__name__
    #         if animal_type not in animals_by_type:
    #             animals_by_type[animal_type] = []
    #         animals_by_type[animal_type].append(
    #             repr(animal))  # add the repr of the animal to the list of animals of the same type
    #
    #     status = f"You have {total_animals_count} animals\n"
    #     for animal_type, animals in animals_by_type.items():  # animals is the __repr__ of an animal object
    #         status += f"----- {len(animals)} {animal_type}:\n"
    #         status += '\n'.join(animals) + '\n'
    #     return status
    #
    # def workers_status(self):
    #     total_workers_count = len(self.workers)
    #     workers_by_type = {}
    #     for worker in self.workers:
    #         worker_type = type(worker).__name__
    #         if worker_type not in workers_by_type:
    #             workers_by_type[worker_type] = []
    #         workers_by_type[worker_type].append(repr(worker))
    #
    #     status = f"You have {total_workers_count} workers\n"
    #     for worker_type, workers in workers_by_type.items():
    #         status += f"----- {len(workers)} {worker_type}:\n"
    #         status += '\n'.join(workers) + '\n'
    #     return status

    def __generate_status(self, objects):
        total_count = len(objects)
        objects_by_type = {}
        for obj in objects:
            obj_type = type(obj).__name__
            if obj_type not in objects_by_type:
                objects_by_type[obj_type] = []
            objects_by_type[obj_type].append(repr(obj))
        status = f"You have {total_count} {objects[0].__class__.__name__.lower()}s\n"
        for obj_type, obj_list in objects_by_type.items():
            status += f"----- {len(obj_list)} {obj_type}:\n"
            status += '\n'.join(obj_list) + '\n'
        return status

    def animals_status(self):
        return self.__generate_status(self.animals)

    def workers_status(self):
        return self.__generate_status(self.workers)
