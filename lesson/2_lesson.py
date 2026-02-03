class Hero:
    def __init__(self, nick, hp, lvl):
        self.nick = nick
        self.hp = hp
        self.lvl = lvl

    def action(self):
        return f"{self.nick} base action activate"

class MageHero(Hero):
    def __init__(self, nick, hp, lvl, mp):
        super().__init__(nick, hp, lvl)
        self.mp = mp

    def action(self):
        return f"Это новый метод дочерного класса {self.nick}"


# asuna = Hero('Asuna', 999, 9999)
# kirito = MageHero("Ardager", 100, 1000)
# print(kirito.nick)
# print(kirito.action())
# print(asuna.action())

class Animal:
    def action(self):
        print(f"Animal action activate")

class Fly(Animal):
    def action(self):
        super().action()
        print(f"Fly action activate")

class Swim(Animal):
    def action(self):
        super().action()
        print(f"Swim action activate")

class Duck(Fly, Swim):
    def action(self):
        super().action()
        print(f"Duck action activate")

donald_duck = Duck()
print(donald_duck.action())
print(Duck.__mro__)