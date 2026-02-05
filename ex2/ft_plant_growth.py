#!/usr/bin/python3

class Plant:
    name: str
    height: int
    age_days: int
    growth_rate: int

    def __init__(self, name: str, height: int, age: int, gowth_rate: int):
        if (name == "" or height < 0 or age < 0 or gowth_rate < 0):
            print("Error: invalid parameters")
            return
        self.name = name.capitalize()
        self.height = height
        self.age_days = age
        self.growth_rate = gowth_rate

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")

    def age(self, amount: int = 1):
        if (amount < 0):
            print("Error: Plant can not age a negative amount")
        self.age_days += amount
        self.grow(amount)

    def grow(self, amount: int = 1):
        if (amount < 0):
            print("Error: Plant can not grow a negative amount")
            return
        self.height += amount * self.growth_rate


def main():
    plant = Plant("Rose", 24, 16, 1)
    plant_old_height = plant.height
    print("=== Day 1 ===")
    plant.print_info()
    for i in range(7):
        plant.age()
    print("== Day 7 ==")
    plant.print_info()
    print(f"Growth this week: +{plant.height - plant_old_height}cm")


if __name__ == "__main__":
    main()
