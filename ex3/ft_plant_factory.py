#!/usr/bin/python3

class Plant:
    name: str
    height: int
    age_days: int
    growth_rate: float

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        gowth_rate: int
    ) -> None:
        if (name == "" or height < 0 or age < 0 or gowth_rate < 0):
            print("Error: invalid parameters")
            return
        self.name = name.capitalize()
        self.height = height
        self.age_days = age
        self.growth_rate = gowth_rate

    def print_info(self) -> None:
        print(f"{self.name} ({self.height}cm, {self.age_days} days)")

    def age(self, amount: int = 1) -> None:
        if (amount < 0):
            print("Error: Plant can not age a negative amount")
        self.age_days += amount
        self.grow(amount)

    def grow(self, amount: int = 1) -> None:
        if (amount < 0):
            print("Error: Plant can not grow a negative amount")
            return
        self.height += amount * self.growth_rate


class PlantFactory:

    def create_plant(
        self, name: str,
        height: float,
        age: int,
        growth_rate: float
    ) -> Plant:
        return Plant(name, height, age, growth_rate)

    def update_name(self, plant: Plant, name: str) -> None:
        plant.set_name(name)

    def update_height(self, plant: Plant, height: float) -> None:
        plant.set_height(height)

    def update_age(self, plant: Plant, age: int) -> None:
        plant.set_age(age)

    def update_growth_rate(self, plant: Plant, growth_rate: float) -> None:
        plant.set_growth_rate(growth_rate)


def main() -> None:
    plants: list[Plant] = []
    plant_factory = PlantFactory()
    plants_counter = 0

    plants.append(plant_factory.create_plant("Rose", 12, 25, 2))
    plants.append(plant_factory.create_plant("Iris", 18, 19, 1))
    plants.append(plant_factory.create_plant("Lily of the valley", 9, 12, 0.5))
    plants.append(plant_factory.create_plant("Primrose", 3, 9, 0.3))
    plants.append(plant_factory.create_plant("Orchidae", 39, 69, 1.2))

    print("=== Plant factory Output ===")
    for plant in plants:
        plant.print_info()
        plants_counter += 1
    print(f"\nTotal plants created: {plants_counter}")


if __name__ == "__main__":
    main()
