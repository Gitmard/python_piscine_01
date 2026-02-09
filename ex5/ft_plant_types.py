#!/usr/bin/python3


class Plant:
    __name: str
    __height: float
    __age: int
    __growth_rate: float

    def __init__(self, name: str, height: float, age: int, gowth_rate: int):
        self.set_name(name.capitalize())
        self.set_height(height)
        self.set_age(age)
        self.set_growth_rate(gowth_rate)

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_growth_rate(self) -> int:
        return self.__growth_rate

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_height(self, height: float) -> None:
        self.__height = height

    def set_age(self, age: int) -> None:
        self.__age = age

    def set_growth_rate(self, growth_rate: float) -> None:
        self.__growth_rate = growth_rate

    def age(self, amount: int = 1) -> None:
        self.grow(amount)

    def grow(self, amount: int = 1) -> None:
        self.set_height(self.get_height() + amount * self.get_growth_rate())

    def to_string(self):
        print(f"{self.get_name()} ({self.get_height()}cm, {self.get_age()} \
days, {self.get_growth_rate()} cm/day)")

    def print_infos(self) -> None:
        print(self.to_string())


class Flower(Plant):
    __color: str

    def __init__(self, name: str, height: float, age: int, growth_rate: float,
                 color: str):
        super().__init__(name, height, age, growth_rate)
        self.set_color(color)

    def get_color(self) -> str:
        return self.__color

    def set_color(self, color: str) -> None:
        self.__color = color

    def bloom(self) -> None:
        print(f"{self.get_name()} is blooming beautifuly !")

    def to_string(self) -> str:
        return (
            f"{self.get_name()} (Flower): \
{self.get_height()}cm, {self.get_age()} days, {self.get_growth_rate()} \
cm/day, {self.get_color()} color"
        )


class Tree(Plant):
    __trunk_diameter: int

    def __init__(self, name: str, height: float, age: int, growth_rate: float,
                 trunk_diameter: int):
        super().__init__(name, height, age, growth_rate)
        self.set_trunk_diameter(trunk_diameter)

    def get_trunk_diameter(self) -> int:
        return self.__trunk_diameter

    def set_trunk_diameter(self, trunk_diameter: int) -> None:
        self.__trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.get_name()} produces a soothing shade")

    def to_string(self):
        return (
                f"{self.get_name()} (Tree): {self.get_height()}cm, \
{self.get_age()} days, {self.get_growth_rate()} cm/day, \
{self.get_trunk_diameter()}cm diameter"
        )


class Vegetable(Plant):
    __harvest_season: str
    __nutritional_value: str

    def __init__(self, name: str, height: float, age: int, growth_rate: float,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age, growth_rate)
        self.set_harvest_season(harvest_season)
        self.set_nutritional_value(nutritional_value)

    def get_harvest_season(self) -> str:
        return self.__harvest_season

    def get_nutritional_value(self) -> str:
        return self.__nutritional_value

    def set_harvest_season(self, harvest_season: str) -> None:
        self.__harvest_season = harvest_season

    def set_nutritional_value(self, nutritional_value: str) -> None:
        self.__nutritional_value = nutritional_value

    def give_nutritional_value(self) -> None:
        print(f"{self.get_name()} is rich in \
{self.get_nutritional_value()}")

    def to_string(self) -> str:
        return (
            f"{self.get_name()} (Vegetable): {self.get_height()}cm, \
{self.get_age()} days, {self.get_growth_rate()} cm/day, \
{self.get_harvest_season()} harvest"
        )


def main():
    oak = Tree("Oak", 534, 32485, 2, 54)
    birch = Tree("Birch", 321, 11680, 1.3, 32)
    rose = Flower("Rose", 12, 24, 0.3, "white")
    iris = Flower("Iris", 19, 21, 0.8, "Pink")
    carrot = Vegetable("Carrot", 8, 12, .25, "Winter", "Fiber")
    cabbage = Vegetable("Cabbage", 4, 29, 1.2, "Winter", "Vitamin C")

    print("=== Garden Plant Type ===")
    print("")
    oak.print_infos()
    oak.produce_shade()
    print("")
    birch.print_infos()
    birch.produce_shade()
    print("")
    rose.print_infos()
    rose.bloom()
    print("")
    iris.print_infos()
    iris.bloom()
    print("")
    carrot.print_infos()
    carrot.give_nutritional_value()
    print("")
    cabbage.print_infos()
    cabbage.give_nutritional_value()


if __name__ == "__main__":
    main()
