#!/usr/bin/python3

class Plant:
    name: str
    height: int
    age: int

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def to_string(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def print_info(self) -> None:
        print(self.to_string())


def main() -> None:
    plants: list[Plant] = []

    plants.append(Plant("Iris", 23, 12))
    plants.append(Plant("Rose", 16, 20))
    plants.append(Plant("Oak", 443, 3687))
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.print_info()


if __name__ == "__main__":
    main()
