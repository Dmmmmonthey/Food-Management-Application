class Recipe:
    def __init__(self, name, ingredients, categories):
        self.name = name
        self.ingredients = ingredients
        self.categories = categories

    def __str__(self):
        return f"{self.name} - Ingredients: {', '.join(self.ingredients)}, Categories: {', '.join(self.categories)}"
