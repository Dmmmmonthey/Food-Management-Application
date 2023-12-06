import unittest
from app.food_management_app import FoodManagementApp
from app.recipe import Recipe
from app.ingredient import Ingredient
from app.dietary_category import DietaryCategory
from app.merge_sort import merge_sort

class TestFoodManagementApp(unittest.TestCase):
    def setUp(self):
        self.food_app = FoodManagementApp()

    def test_add_recipe(self):
        recipe = Recipe("Pasta", ["Pasta", "Tomato Sauce"], "Boil pasta. Mix with sauce.", ["Vegetarian", "Italian"])
        self.food_app.add_recipe(recipe)

        recipes = self.food_app.get_recipes()
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0], recipe)

    def test_get_recipes(self):
        # Test whether get_recipes returns a list of Recipe instances
        recipes = self.food_app.get_recipes()
        self.assertIsInstance(recipes, list)
        self.assertTrue(all(isinstance(recipe, Recipe) for recipe in recipes))

    def test_get_dietary_categories(self):
        # Test whether get_dietary_categories returns a list of DietaryCategory instances
        categories = self.food_app.get_dietary_categories()
        self.assertIsInstance(categories, list)
        self.assertTrue(all(isinstance(category, DietaryCategory) for category in categories))

class TestRecipe(unittest.TestCase):
    def test_recipe_creation(self):
        recipe = Recipe("Salad", ["Lettuce", "Tomato", "Cucumber"], "Mix all ingredients.", ["Vegetarian", "Healthy"])
        self.assertEqual(recipe.name, "Salad")
        self.assertEqual(recipe.ingredients, ["Lettuce", "Tomato", "Cucumber"])
        self.assertEqual(recipe.preparation_steps, "Mix all ingredients.")
        self.assertEqual(recipe.dietary_categories, ["Vegetarian", "Healthy"])

    def test_recipe_attributes(self):
        recipe = Recipe("Soup", ["Carrot", "Onion", "Broth"],

