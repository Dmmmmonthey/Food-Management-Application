from app.recipe import Recipe
from app.merge_sort import merge_sort

class FoodManagementApp:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def print_recipes(self):
        for recipe in self.recipes:
            print(recipe)

# Example usage
if __name__ == "__main__":
    app = FoodManagementApp()

    # Sample recipes
    recipe1 = Recipe("Pasta Carbonara", ["Spaghetti", "Bacon", "Eggs", "Parmesan"], ["Italian", "Pasta"])
    recipe2 = Recipe("Chicken Stir-Fry", ["Chicken", "Broccoli", "Soy Sauce"], ["Asian", "Chicken", "Vegetables"])

    app.add_recipe(recipe1)
    app.add_recipe(recipe2)

    # Print unsorted recipes
    print("Unsorted Recipes:")
    app.print_recipes()

    # Sort recipes by name using merge sort
    sorted_recipes = merge_sort(app.recipes, key=lambda x: x.name)
    app.recipes = sorted_recipes

    # Print sorted recipes
    print("\nSorted Recipes by Name:")
    app.print_recipes()
