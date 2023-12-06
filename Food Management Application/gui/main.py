from app.food_management_app import FoodManagementApp
from app.recipe import Recipe
from app.merge_sort import merge_sort

def display_recipes(recipes):
    for i, recipe in enumerate(recipes, start=1):
        print(f"{i}. {recipe.name}: {recipe.ingredients} - {recipe.preparation_steps}")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    food_app = FoodManagementApp()

    while True:
        print("\nFood Management Application Menu:")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Exit")

        choice = get_user_choice()

        if choice == 1:
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(", ")
            preparation_steps = input("Enter preparation steps: ")
            dietary_categories = input("Enter dietary categories (comma-separated): ").split(", ")

            recipe = Recipe(name, ingredients, preparation_steps, dietary_categories)
            food_app.add_recipe(recipe)
            print(f"Recipe '{name}' added successfully!")

        elif choice == 2:
            sorting_choice = input("Sort recipes by (1) Name or (2) Ingredients: ")
            key = lambda x: (x.name, x.ingredients) if sorting_choice == "1" else (x.ingredients, x.name)
            sorted_recipes = merge_sort(food_app.get_recipes(), key=key)

            print("\nSorted Recipes:")
            display_recipes(sorted_recipes)

        elif choice == 3:
            print("Exiting Food Management Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    # Display message and wait for a key press before closing
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()



