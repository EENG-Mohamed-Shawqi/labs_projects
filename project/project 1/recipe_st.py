import pandas as pd
import os
import random

recipes = "recipes.csv"

def check_ex(df_recipes):
    """
    By Mohamed Shawqi
    This function is to check whether the file exist
    to avoid re-writing the columns file while adding a new recipe
    """

    if os.path.exists(recipes):
        df_recipes.to_csv(recipes, mode='a', header=False, index=False)
        print('recipies has been updated!')
    else:
        df_recipes.to_csv(recipes, mode='w', header=True, index=False)
        print('recipies file has been created!')


def save_new_recipe(category, recipe_name, ingredients, preptime, instruction, Difficulty):
    """
    By Mohamed Shawqi
    This function is to take variable values from streamlit
    to add into the recipe collection

    """

    if ingredients:
        ingredients = [i.strip() for i in ingredients.lower().split(",")]

    new_recipe = [{'category': category.lower(),
                   'recipe_name': recipe_name.lower(),
                   'ingredients': ingredients,
                   'prep_time': preptime,
                   'instruction': instruction.lower(),
                   'Difficulty': Difficulty.lower()}]

    df_new_recipe = pd.DataFrame(new_recipe)
    check_ex(df_new_recipe)



def view_all():
    """
    By Ali Alsaeed this function is to
    View all the recipes if they exist
    """

    df = pd.read_csv(recipes)


    return df[['recipe_name', 'prep_time']]

def randomizer():
    """
    By Ali Alsaeed this function is to
    Give a random recipe from the csv file
    """


    df = pd.read_csv(recipes)


    random_index = random.randint(0,len(df)-1)
    return df.iloc[[random_index]]


def find_by_ingredient(ingredient):
    """
 By Ali Hussain this function is to
    search for an recipe by the ingredient
    """
    

    df = pd.read_csv(recipes)

    

    ingredient = ingredient.lower()
    matching_recipes = df[
        df["ingredients"].str.lower().str.contains(ingredient)
    ]
    return matching_recipes


def display_menu():
    """Display the main menu options."""
    print("\n=== Recipe Manager===")
    print("1. Add a new recipe to the collection")
    print("2. Search for recipes by ingredient")
    print("3. View all recipes")
    print("4. View a random recipe suggestion")
    print("5. Exit")
    return int(input("Enter your choice (1-5): "))

def main():

    while True:
        choice = display_menu()
        if choice == 1:
            add_new_recipe()
        elif choice == 2:
            search_by_ingredient()

        elif choice == 3:
            view_all()

        elif choice == 4:
            randomizer()

        elif choice == 5:
            print("Thank you for using Recipe manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()