#!/usr/bin/python3

class Plant:
    name: str
    height: int
    age: int

    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    plants: list[Plant] = []

    plants.append(Plant("Iris", 23, 12))
    plants.append(Plant("Rose", 16, 20))
    plants.append(Plant("Oak", 443, 3687))
    for plant in plants:
        plant.print_info()


if __name__ == "__main__":
    main()
