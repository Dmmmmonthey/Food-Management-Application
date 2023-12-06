class FoodManagementApp:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_recipes(self):
        return self.recipes

    def get_dietary_categories(self):
        categories = set()
        for recipe in self.recipes:
            categories.update(recipe.dietary_categories)
        return list(categories)


