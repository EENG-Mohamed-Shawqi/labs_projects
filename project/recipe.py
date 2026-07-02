import pandas as pd
import os
import random

recipes="recipes.csv"

def check_ex(df_recipes):
    """
    By Mohamed Shawqi
    This function is to check whether the file exist
    to avoid overwriting the file while adding a new recipe
    """

    if os.path.exists(recipes):
        df_recipes.to_csv(recipes,mode='a',header=False,index=False)
        print('recipies has been updated!')
    else:
        df_recipes.to_csv(recipes,mode='w',header=True,index=False)
        print('recipies file has been created!')


def add_new_recipe():
    """
    By Mohamed Shawqi
    This function is to add new recipe
    """

    while True:
            category=input('Enter the recipe category(Breakfast, Lunch, Dinner, Dessert)').lower()
            if (category=='breakfast') or (category=='lunch') or (category=='dinner') or (category=='dessert'):
                break
            else:
                print('Please type Breakfast, Lunch, Dinner or Dessert.')
                
    while True:
        recipe_name=input('Enter the recipe name').strip().lower()
        if not recipe_name:
            print("Assign the recipe name!")
        else:
            break

    while True:
        ingredients = input("Enter the ingredients (separated by commas): ").strip().lower().split(",")
        if ingredients==['']:
            print("Type at least one ingredient")
        else:
            break

    while True:
        try:
            preptime=int(input('Enter the preperation time in minuts'))
            if preptime!=0:
                break
        except ValueError:
            print("Please enter a valid integer number.")
    
    while True:
            instruction=input("Enter the cooking instructions").strip().lower()
            if not instruction:
                print("Type 'none' if there is no instructions")
            else: 
                break

    while True:
            Difficulty=input('Enter the difficulty (Easy, Medium, Hard)').lower()
            if (Difficulty=='easy') or (Difficulty=='medium') or (Difficulty=='hard'):
                break
            else:
                print('Please type Easy, Medium, or Hard.')


    new_recipe=[{'category':category,
                 'recipe_name':recipe_name,
                 'ingredients':ingredients,
                 'prep_time':preptime,
                 'instruction':instruction,
                 'Difficulty':Difficulty,}]

    df_new_recipe=pd.DataFrame(new_recipe)
    check_ex(df_new_recipe)



def view_all():
    """
    By Ali Alsaeed this function is to
    View all the recipes if they exist
    """
    recipes = "recipes.csv"
    if not os.path.exists(recipes):
        return print('There is no such file name!')

    df = pd.read_csv(recipes)

    if df.empty:
        return print('There is no recipes yet!')


    return display(df[['recipe_name', 'prep_time']])

def randomizer():
    """
    By Ali Alsaeed this function is to
    Give a random recipe from the csv file
    """

    if not os.path.exists(recipes):
        return print('There is no such file name!')

    df = pd.read_csv(recipes)

    if df.empty:
        return print('There is no recipes yet!')

    random_index = random.randint(0,len(df)-1)
    return display(df.iloc[[random_index]])


def search_by_ingredient():
    """
    By Ali Hussain this function is to
    search for an recipe by the ingredient
    """

    if not os.path.exists(recipes):
        return print('There is no such file name! \n choose 1 to create a file.')

    df = pd.read_csv(recipes)

    if df.empty:
        return print('There is no recipes yet! \n choose 1 to create add recipe.')

    ingredient = input("Enter an ingredient: ").lower()

    matching_recipes = df[
        df["ingredients"].str.lower().str.contains(ingredient)
    ]

    if matching_recipes.empty:
        print(f"\nNo recipes found with '{ingredient}'.")
        return
    else:
        print(f"\nRecipes containing '{ingredient}':")
        return display(matching_recipes)




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