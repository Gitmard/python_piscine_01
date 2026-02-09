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

    def print_info(self) -> None:
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")

    def to_string(self):
        print(f"{self.get_name()} ({self.get_height()}cm, {self.get_age()} \
days, {self.get_growth_rate()} cm/day)")


class GardenSecuritySystem:
    def log(self, message: str) -> None:
        print(f"[GardenSecuritySystem] {message}")

    def check_name(self, name: str) -> bool:
        instance_ok = isinstance(name, str)
        value_ok = name != ""
        if not instance_ok:
            self.log("Non string name rejected")
        if not value_ok:
            self.log("Empty name rejected")
        return instance_ok and value_ok

    def check_height(self, height: float) -> bool:
        instance_ok = isinstance(height, float) or isinstance(height, int)
        value_ok = height >= 0
        if not instance_ok:
            self.log("Non float height rejected")
        if not value_ok:
            self.log("Negative height rejected")
        return instance_ok and value_ok

    def check_age(self, age: int) -> bool:
        instance_ok = isinstance(age, int)
        value_ok = age >= 0
        if not instance_ok:
            self.log("Non int age rejected")
        if not value_ok:
            self.log("Negative age rejected")
        return instance_ok and value_ok

    def check_growth_rate(self, growth_rate: float) -> bool:
        instance_ok = isinstance(growth_rate, float) or isinstance(growth_rate,
                                                                   int)
        value_ok = growth_rate >= 0
        if not instance_ok:
            self.log("Non float growth rate rejected")
        if not value_ok:
            self.log("Negative growth rate rejected")
        return instance_ok and value_ok

    def check_plant(self, plant: Plant):
        if not self.check_name(plant.get_name()):
            return False
        if not self.check_height(plant.get_height()):
            return False
        if not self.check_age(plant.get_age()):
            return False
        if not self.check_growth_rate(plant.get_growth_rate()):
            return False
        return True


class PlantFactory:
    __garden_security_system: GardenSecuritySystem

    def __init__(self):
        self.__garden_security_system = GardenSecuritySystem()

    def log(self, message: str) -> None:
        print(f"[PlantFactory] {message}")

    def create_plant(self, name: str, height: float, age: int,
                     growth_rate: float) -> Plant | None:
        new_plant = Plant(name, height, age, growth_rate)
        if self.__garden_security_system.check_plant(new_plant):
            self.log(f"Plant created: {new_plant.get_name()}")
            return new_plant
        self.log("[PlantFactory] Invalid plant creation operation [REJECTED]")
        return None

    def update_name(self, plant: Plant, name: str) -> bool:
        if not self.__garden_security_system.check_name(name):
            self.log(f"Invalid operation attempted: name {name} [REJECTED]")
            return False
        plant.set_name(name)
        self.log(f"Name updated: \"{name}\" [OK]")
        return True

    def update_height(self, plant: Plant, height: float) -> bool:
        if not self.__garden_security_system.check_height(height):
            self.log(f"Invalid operation attempted: height {height}cm \
                [REJECTED]")
            return False
        plant.set_height(height)
        self.log(f"Height updated: {height}cm [OK]")
        return True

    def update_age(self, plant: Plant, age: int) -> bool:
        if not self.__garden_security_system.check_age(age):
            self.log(f"Invalid operation attempted: age {age}")
            return False
        plant.set_age(age)
        self.log(f"Age updated: {age} days [OK]")
        return True

    def update_growth_rate(self, plant: Plant, growth_rate: float) -> bool:
        if not self.__garden_security_system.check_growth_rate(growth_rate):
            self.log(f"Invalid operation attempted: growth rate {growth_rate}/\
                day [REJECTED]")
            return False
        plant.set_growth_rate(growth_rate)
        self.log(f"Growth rate updated: {growth_rate}cm/day [OK]")
        return True


def main():
    print("=== Garden Security System ===")
    plant: Plant
    plant_factory = PlantFactory()

    print("\n")
    plant = plant_factory.create_plant("Rose", 12, 8, 0.25)
    plant_factory.update_age(plant, 12)
    plant_factory.update_height(plant, 54)

    print("\n")
    plant_factory.update_name(plant, 12)
    plant_factory.update_age(plant, -42)

    print("\n")
    print(f"Current plant: {plant.to_string()}")


if __name__ == "__main__":
    main()
