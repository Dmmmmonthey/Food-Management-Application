# app/food_management_app.py

from app.merge_sort import insertion_sort

class FoodManagementApp:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        insertion_sort(self.recipes, key=lambda x: x.name)

    def print_recipes(self):
        for recipe in self.recipes:
            print(recipe)

