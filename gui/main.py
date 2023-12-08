# gui/main.py

from app.food_management_app import FoodManagementApp
from tkinter import Tk, Label, Button

class FoodManagementAppGUI:
    def __init__(self, root, app):
        self.root = root
        self.root.title("Food Management App")

        self.app = app

        self.label = Label(root, text="Food Management App")
        self.label.pack()

        self.add_recipe_button = Button(root, text="Add Sample Recipe", command=self.add_sample_recipe)
        self.add_recipe_button.pack()

    def add_sample_recipe(self):
        # Add a sample recipe to the app
        sample_recipe = Recipe("Sample Recipe", ["Ingredient1", "Ingredient2"], ["Category1", "Category2"])
        self.app.add_recipe(sample_recipe)

        # Print the recipes
        print("Recipes after adding a sample recipe:")
        self.app.print_recipes()

# Example usage
def main():
    app = FoodManagementApp()

    root = Tk()
    gui = FoodManagementAppGUI(root, app)
    root.mainloop()

if __name__ == "__main__":
    main()


