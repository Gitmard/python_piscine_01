#!/usr/bin/python3

class Plant:
    name: str
    height: int
    age_days: int
    growth_rate: float

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
    plants: list[Plant] = []
    plants_counter = 0

    plants.append(Plant("Rose", 12, 25, 2))
    plants.append(Plant("Iris", 18, 19, 1))
    plants.append(Plant("Lily of the valley", 9, 12, 0.5))
    plants.append(Plant("Primrose", 3, 9, 0.3))
    plants.append(Plant("Orchidae", 39, 69, 1.2))

    print("=== Plant factory Output ===")
    for plant in plants:
        plant.print_info()
        plants_counter += 1
    print(f"\nTotal plants created: {plants_counter}")


if __name__ == "__main__":
    main()
