from enum import Flag, auto
from datetime import datetime
from typing import Self


class Dish:
    def __init__(self, name: str, ingredients: list[str], calories: int) -> None:
        self.name = name
        self.ingredients = ingredients
        self.calories = calories

    @staticmethod
    def from_dict(source: dict) -> Self:
        dish = Dish(source["name"], source["ingredients"])

        if "calories" in source:
            dish.calories = source["calories"]

        return dish

    def to_dict(self: Self) -> dict:
        dest = {"name": self.name, "ingredients": self.ingredients}

        if self.calories:
            dest["calories"] = self.calories

        return dest

    def __repr__(self: Self):
        return f"City(\
                name={self.name}, \
                ingredients={self.ingredients}, \
                calories={self.calories}\
            )"


class Meal(Flag):
    BREAKFAST = auto()
    SECOND_BREAKFAST = auto()
    BRUNCH = auto()
    ELEVENSIES = auto()
    LUNCH = auto()
    AFTERNOON_TEA = auto()
    LINNER = auto()
    HIGH_TEA = auto()
    DINNER = auto()
    SUPPER = auto()
    MIDNIGHT_SNACK = auto()


class Menu:
    def __init__(self, date: datetime, meal: Meal, dishes: list[Dish]) -> None:
        self.date = date
        self.meal = meal
        self.dishes = dishes

    @staticmethod
    def from_dict(source: dict) -> Self:
        return Menu(source["date"], source["meal"], source["dishes"])

    def to_dict(self: Self) -> dict:
        return {"date": self.date, "meal": self.meal, "ingredients": self.dishes}

    def __repr__(self):
        return f"Menu(\
                date={self.date}, \
                meal={self.meal}, \
                dishes={self.dishes}\
            )"
