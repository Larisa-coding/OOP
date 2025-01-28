class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} жует кабачки в кожуре.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} говорит чикчирики")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} говорит ррррр!")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} говорит шшшш!")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def save_zoo(self, filename):
        with open(filename, 'w') as file:
            for animal in self.animals:
                file.write(f"{animal.__class__.__name__},{animal.name},{animal.age}\n")
            for staff_member in self.staff:
                file.write(f"{staff_member.__class__.__name__},{staff_member.name}\n")

    def load_zoo(self, filename):
        self.animals.clear()
        self.staff.clear()
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:  # Animal
                    class_name, name, age = parts
                    if class_name == 'птичка':
                        self.animals.append(Bird(name, int(age), 0))
                    elif class_name == 'тигрр':
                        self.animals.append(Mammal(name, int(age), ''))
                    elif class_name == 'змеючка':
                        self.animals.append(Reptile(name, int(age), ''))
                elif len(parts) == 2:  # Staff
                    class_name, name = parts
                    if class_name == 'владелец зуу':
                        self.staff.append(ZooKeeper(name))
                    elif class_name == 'ветеринар':self.staff.append(Veterinarian(name))

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

if __name__ == "__main__":

    parrot = Bird("птичка", 2, 25)
    tiger = Mammal("тигрр", 4, "рыжий")
    snake = Reptile("змеючка", 3, "скользкая")

    zookeeper = ZooKeeper("Алиска")
    vet = Veterinarian("Олежка")

    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(tiger)
    zoo.add_animal(snake)
    zoo.add_staff(zookeeper)
    zoo.add_staff(vet)

    animal_sound(zoo.animals)

    zookeeper.feed_animal(tiger)
    vet.heal_animal(snake)

    zoo.save_zoo("zoo_data.txt")
    zoo.load_zoo("zoo_data.txt")