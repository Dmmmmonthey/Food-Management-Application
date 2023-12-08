# app/recipe.py

class Recipe:
    def __init__(self, name, ingredients, categories):
        self.name = name
        self.ingredients = ingredients
        self.categories = categories

    def __str__(self):
        return f"Recipe: {self.name}, Ingredients: {self.ingredients}, Categories: {self.categories}"
