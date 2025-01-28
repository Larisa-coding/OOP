from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "мечом"

class Bow(Weapon):
    def attack(self):
        return "из лука"

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.attack()}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} наносит удар {self.weapon.attack()}.")
        else:
            print(f"{self.name} не выбрал оружие!")

class Monster:
    def defeat(self):
        print("Монстр побежден!")

def main():
    fighter = Fighter("Боец")
    monster = Monster()

    sword = Sword()
    bow = Bow()

    fighter.change_weapon(sword)
    fighter.attack()
    monster.defeat()

    print()

    fighter.change_weapon(bow)
    fighter.attack()
    monster.defeat()

if __name__ == "__main__":
    main()