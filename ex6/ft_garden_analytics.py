#!/usr/bin/python3


class Plant:
    __name: str
    __height: float
    __age: int
    __growth_rate: float

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth_rate: float
    ):
        self.set_name(name.capitalize())
        self.set_height(height)
        self.set_age(age)
        self.set_growth_rate(growth_rate)

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_growth_rate(self) -> float:
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
        return (
            f"{self.get_name()}" +
            f"({self.get_height()}cm, " +
            f"{self.get_age()}cm, "
            f"{self.get_age()} days, "
            f"{self.get_growth_rate()} cm/day)"
        )

    def print_infos(self) -> None:
        print(self.to_string())


class FloweringPlant(Plant):
    __color: str

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth_rate: float,
            color: str
    ):
        super().__init__(name, height, age, growth_rate)
        self.set_color(color)

    def get_color(self) -> str:
        return self.__color

    def set_color(self, color: str) -> None:
        self.__color = color

    def to_string(self):
        return (
            f"{self.get_name()}" +
            f"({self.get_height()}cm, " +
            f"{self.get_age()}cm, "
            f"{self.get_age()} days, "
            f"{self.get_growth_rate()} cm/day, ",
            f"{self.get_color()})"
        )


class PrizeFlower(FloweringPlant):
    __prize_points: int

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth_rate: float,
            color: str,
            prize_points: int
    ):
        super().__init__(name, height, age, growth_rate, color)
        self.set_prize_points(prize_points)

    def get_prize_points(self) -> int:
        return self.__prize_points

    def set_prize_points(self, prize_points: int) -> None:
        self.__prize_points = prize_points

    def to_string(self):
        return (
            f"{self.get_name()}" +
            f"({self.get_height()}cm, " +
            f"{self.get_age()}cm, "
            f"{self.get_age()} days, "
            f"{self.get_growth_rate()} cm/day, ",
            f"{self.get_color()}, " +
            f"{self.get_prize_points()} points)"
        )


class GardenSecuritySystem:

    @classmethod
    def log(cls, message: str) -> None:
        print(f"[GardenSecuritySystem] {message}")

    @classmethod
    def check_string_attribute(cls, value: str, name: str,
                               allow_empty_string: bool = False) -> bool:
        instance_ok = isinstance(value, str)
        value_ok = allow_empty_string or value != ""
        if not instance_ok:
            cls.log(f"Non string {name} rejected")
        if not value_ok:
            cls.log(f"Empty {name} rejected")
        return instance_ok and value_ok

    @classmethod
    def check_int_attibute(cls, value: int, name: str, allow_negative: bool =
                           False) -> bool:
        instance_ok = isinstance(value, int)
        value_ok = allow_negative or value >= 0
        if not instance_ok:
            cls.log(f"Non int {name} rejected")
        if not value_ok:
            cls.log(f"Negative {name} rejected")
        return instance_ok and value_ok

    @classmethod
    def check_float_attribute(cls, value: float, name: str,
                              allow_negative: bool = False) -> bool:
        instance_ok = isinstance(value, float) or isinstance(value, int)
        value_ok = allow_negative or value >= 0
        if not instance_ok:
            cls.log(f"Non float {name} rejected")
        if not value_ok:
            cls.log(f"Negative {name} rejected")
        return instance_ok and value_ok

    @classmethod
    def check_plant(cls, plant: Plant) -> bool:
        if not cls.check_string_attribute(plant.get_name(), "name"):
            return False
        if not cls.check_float_attribute(plant.get_height(), "height"):
            return False
        if not cls.check_int_attibute(plant.get_age(), "age"):
            return False
        if not cls.check_float_attribute(
                plant.get_growth_rate(),
                "growth rate"
        ):
            return False
        return True

    @classmethod
    def check_flowering_plant(cls, flowering_plant: FloweringPlant) -> bool:
        if not cls.check_string_attribute(flowering_plant.get_name(), "name"):
            return False
        return cls.check_plant(flowering_plant)

    @classmethod
    def check_prize_flower(cls, prize_flower: PrizeFlower) -> bool:
        if not cls.check_string_attribute(prize_flower.get_name(), "name"):
            return False
        return cls.check_flowering_plant(prize_flower)


class PlantFactory:

    @classmethod
    def log(
            cls,
            message: str
    ) -> None:
        print(f"[PlantFactory] {message}")

    @classmethod
    def create_plant(
            cls,
            name: str,
            height: float,
            age: int,
            growth_rate: float
    ) -> Plant:
        new_plant = Plant(name, height, age, growth_rate)
        if GardenSecuritySystem.check_plant(new_plant):
            cls.log(f"Plant created: {new_plant.get_name()}")
            return new_plant
        cls.log(
            "Invalid plant creation operation" +
            "[REJECTED]"
        )
        return None

    @classmethod
    def create_flowering_plant(
            cls,
            name: str,
            height: float,
            age: int,
            growth_rate: float,
            color: str
    ) -> Plant:
        new_plant = FloweringPlant(name, height, age, growth_rate, color)
        if GardenSecuritySystem.check_flowering_plant(new_plant):
            cls.log(f"Plant created: {new_plant.get_name()}")
            return new_plant
        cls.log(
            "Invalid flowering plant creation operation" +
            "[REJECTED]"
        )
        return None

    @classmethod
    def create_prize_flower(
            cls,
            name: str,
            height: float,
            age: int,
            growth_rate: float,
            color: str,
            prize_points: int
    ) -> PrizeFlower:
        new_plant = PrizeFlower(
            name,
            height,
            age,
            growth_rate,
            color,
            prize_points
        )
        if GardenSecuritySystem.check_prize_flower(new_plant):
            cls.log(f"Plant created: {new_plant.get_name()}")
            return new_plant
        cls.log(
            "Invalid prize flower creation operation" +
            "[REJECTED]"
        )
        return None

    @classmethod
    def update_name(
            cls,
            plant: Plant,
            name: str
    ) -> bool:
        if not GardenSecuritySystem.check_string_attribute(name, "name"):
            cls.log(
                f"Invalid operation attempted: name {name}" +
                "[REJECTED]"
            )
            return False
        plant.set_name(name)
        cls.log(f"Name updated: \"{name}\" [OK]")
        return True

    @classmethod
    def update_height(
            cls,
            plant: Plant,
            height: float
    ) -> bool:
        if not GardenSecuritySystem.check_float_attribute(height, "height"):
            cls.log(
                f"Invalid operation attempted: height {height}cm" +
                "[REJECTED]"
            )
            return False
        plant.set_height(height)
        cls.log(f"Height updated: {height}cm [OK]")
        return True

    @classmethod
    def update_age(
            cls,
            plant: Plant,
            age: int
    ) -> bool:
        if not GardenSecuritySystem.check_int_attibute(age, "age"):
            cls.log(f"Invalid operation attempted: age {age}")
            return False
        plant.set_age(age)
        cls.log(f"Age updated: {age} days [OK]")
        return True

    @classmethod
    def update_growth_rate(
            cls,
            plant: Plant,
            growth_rate: float
    ) -> bool:
        if not GardenSecuritySystem.check_float_attribute(
                growth_rate,
                "growth rate"
        ):
            cls.log(
                f"Invalid operation attempted: growth rate {growth_rate}/day" +
                "[REJECTED]")
            return False
        plant.set_growth_rate(growth_rate)
        cls.log(f"Growth rate updated: {growth_rate}cm/day [OK]")
        return True


class Gardener:
    __name: str

    def __init__(self, name: str):
        self.set_name(name)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name


class Garden:
    __gardener: Gardener
    __plants: list[Plant]
    __score: int
    __total_growth: float

    def __init__(
            self,
            gardener: Gardener
    ):
        self.set_gardener(gardener)
        self.__plants = []
        self.__score = 0
        self.__total_growth = 0

    def get_gardener(self) -> Gardener:
        return self.__gardener

    def set_gardener(self, gardener: Gardener) -> None:
        self.__gardener = gardener

    def get_plants(self) -> list[Plant]:
        return self.__plants

    def add_plant(self, plant: Plant) -> None:
        self.get_plants().append(plant)
        if isinstance(plant, PrizeFlower):
            self.set_score(self.get_score() + plant.get_prize_points())
        print(
            f"Added {plant.get_name()} to",
            f"{self.get_gardener().get_name()}'s garden"
        )

    def remove_plant(self, plant: Plant) -> None:
        self.get_plants().remove(plant)

    def get_score(self) -> int:
        return self.__score

    def set_score(self, score: int) -> None:
        self.__score = score

    def get_total_growth(self) -> float:
        return self.__total_growth

    def set_total_growth(self, total_growth: float) -> None:
        self.__total_growth = total_growth

    def grow_all(self) -> None:
        total_growth = 0.0

        for plant in self.get_plants():
            plant.grow()
            total_growth += plant.get_growth_rate()
            print(
                f"{plant.get_name().capitalize()}",
                f"grew {plant.get_growth_rate()}cm"
            )
        self.set_total_growth(self.get_total_growth() + total_growth)


class GardenManager:
    __gardens: dict[str, list[Garden]]

    def __init__(self, gardens: dict[str, list[Garden]]):
        self.__gardens = gardens

    def get_gardens(self) -> dict[str, list[Garden]]:
        return self.__gardens

    def create_garden(self, gardener_name: str) -> Garden:
        garden = Garden(Gardener(gardener_name))
        self.add_garden(garden)
        return garden

    def add_garden(self, garden: Garden) -> None:
        if not garden.get_gardener().get_name() in self.get_gardens().keys():
            self.get_gardens()[garden.get_gardener().get_name()] = []
        self.get_gardens()[garden.get_gardener().get_name()].append(garden)

    def remove_garden(self, garden: Garden) -> None:
        self.get_gardens()[garden.get_gardener().get_name()].remove(garden)

    @staticmethod
    def grow_garden(garden: Garden) -> None:
        print(
            f"{garden.get_gardener().get_name()}",
            "is helping all plants grow..."
        )
        garden.grow_all()

    def print_garden_stats(self, garden: Garden) -> None:
        self.GardenStats.print_garden_stats(garden, self.get_gardens())

    class GardenStats:

        @staticmethod
        def __print_garden_specific_stats(garden: Garden) -> None:
            garden_counters: dict[str, int] = {
                "regular": 0,
                "flowering": 0,
                "prize": 0
            }

            for plant in garden.get_plants():
                if isinstance(plant, PrizeFlower):
                    print(
                        f"{plant.get_name()}:",
                        f"{plant.get_height()}cm,",
                        f"{plant.get_age()}days,",
                        f"{plant.get_growth_rate()}cm/day,",
                        f"{plant.get_color()} flowers (blooming),",
                        f"Prize points: {plant.get_prize_points()}",
                    )
                    garden_counters["regular"] += 1
                elif isinstance(plant, FloweringPlant):
                    print(
                        f"{plant.get_name()}:",
                        f"{plant.get_height()}cm,",
                        f"{plant.get_age()}days,",
                        f"{plant.get_growth_rate()}cm/day,",
                        f"{plant.get_color()} flowers (blooming)"
                    )
                    garden_counters["flowering"] += 1
                elif isinstance(plant, Plant):
                    print(
                        f"{plant.get_name()}:",
                        f"{plant.get_height()}cm,",
                        f"{plant.get_age()}days,",
                        f"{plant.get_growth_rate()}cm/day"
                    )
                    garden_counters["prize"] += 1
            print(
                f"Plants added: {len(garden.get_plants())}, ",
                f"Total growth: {garden.get_total_growth()}"
            )

        @staticmethod
        def __print_garden_scores(gardens: dict[str, list[Garden]]) -> None:
            garden_scores_str = "Garden scores - "
            scores: dict[str, int] = {}
            i = 0

            for gardener_name in gardens.keys():
                scores[gardener_name] = 0
                for garden in gardens[gardener_name]:
                    scores[gardener_name] += garden.get_score()
            for name, score in scores.items():
                garden_scores_str += f"{name}: {scores[name]}"
                if i < len(scores) - 1:
                    garden_scores_str += ", "
                i += 1
            print(garden_scores_str)

        @classmethod
        def print_garden_stats(
                cls,
                garden: Garden,
                gardens: dict[str, list[Garden]]
        ) -> None:
            print(
                f"=== {garden.get_gardener().get_name().capitalize()}'s",
                "Garden Report ==="
            )
            print("Plants in garden :")
            cls.__print_garden_specific_stats(garden)
            print("")
            cls.__print_garden_scores(gardens)
            print(f"Total gardens managed: {len(gardens)}")

def main():
    simards_garden: Garden
    garden_manager = GardenManager({})
    simards_plants: list[Plant] = [
        Plant(
            "Oak Tree",
            564.0,
            48180,
            0.15
        ),
        FloweringPlant(
            "Sunflower",
            56.0,
            12,
            0.6,
            "Yellow"
        ),
        PrizeFlower(
            "Rose",
            23.0,
            32,
            0.2,
            "Red",
            12
        ),
        PrizeFlower(
            "Lily of the valley",
            4.0,
            8,
            0.1,
            "Blue",
            24
        ),
    ]
    jean_phils_plants = [
        PrizeFlower(
            "Orchidae",
            32,
            54,
            0.98,
            "Yellow",
            69
        ),
        PrizeFlower(
            "Poppy",
            8,
            12,
            0.3,
            "Red",
            45
        )
    ]
    print("=== Garden Management System Demo ===\n")

    simards_garden = garden_manager.create_garden("Simard")
    jean_phils_garden = garden_manager.create_garden("Jean Phil Monslip")

    for plant in simards_plants:
        simards_garden.add_plant(plant)
    for plant in jean_phils_plants:
        jean_phils_garden.add_plant(plant)
    print("")
    GardenManager.grow_garden(simards_garden)
    print("")
    GardenManager.grow_garden(jean_phils_garden)
    print("")
    garden_manager.print_garden_stats(simards_garden)
    print("")
    garden_manager.print_garden_stats(jean_phils_garden)

if __name__ == "__main__":
    main()
