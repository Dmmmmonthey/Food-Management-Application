import unittest
from app.food_management_app import FoodManagementApp, Recipe

class TestFoodManagementApp(unittest.TestCase):
    def setUp(self):
        self.app = FoodManagementApp()

    def test_add_recipe(self):
        recipe = Recipe("Test Recipe", ["Ingredient1", "Ingredient2"], ["Category1", "Category2"])
        self.app.add_recipe(recipe)
        self.assertEqual(len(self.app.recipes), 1)

    def test_print_recipes(self):
        recipe = Recipe("Test Recipe", ["Ingredient1", "Ingredient2"], ["Category1", "Category2"])
        self.app.add_recipe(recipe)

        # Redirect print output to a variable for testing
        import io
        from contextlib import redirect_stdout

        with io.StringIO() as buffer, redirect_stdout(buffer):
            self.app.print_recipes()
            output = buffer.getvalue().strip()

        expected_output = "Test Recipe - Ingredients: Ingredient1, Ingredient2, Categories: Category1, Category2"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()

