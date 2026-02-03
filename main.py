class Animal:
    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def description(self):
        return f"{self.name}, возраст:{self.age}, скорость:{self.speed}"

    def increase_speed(self):
        self.speed += 10
        return f"Скорость увеличился до:{self.speed}"

tiger = Animal("tiger", 3, 80)
snake = Animal("snake", 2, 70)
print(tiger.description())
print(snake.description())
print(tiger.increase_speed())