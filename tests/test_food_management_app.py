# tests/test_food_management_app.py

import unittest
from app.food_management_app import FoodManagementApp, Recipe

class TestFoodManagementApp(unittest.TestCase):
    def test_add_recipe(self):
        app = FoodManagementApp()
        recipe = Recipe("Test Recipe", ["Test Ingredient"], ["Test Category"])
        app.add_recipe(recipe)
        self.assertEqual(len(app.recipes), 1)
        self.assertEqual(app.recipes[0].name, "Test Recipe")

if __name__ == "__main__":
    unittest.main()


