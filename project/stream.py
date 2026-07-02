import streamlit as st
import recipe_st as rm

st.set_page_config(page_title="Recipe Manager")

# start page
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to(page_name):
    st.session_state.page = page_name

# Home page
if st.session_state.page == "home":
    st.title(" Recipe Manager 👨‍🍳")
    st.write("Welcome!")
    st.write("Choose an option:")

    st.button(" Add a new recipe", on_click=go_to, args=("add",), use_container_width=True)
    st.button(" Search by ingredient", on_click=go_to, args=("search",), use_container_width=True)
    st.button(" View all recipes", on_click=go_to, args=("view",), use_container_width=True)
    st.button(" Random recipe", on_click=go_to, args=("random",), use_container_width=True)
    st.button(" Exit", on_click=go_to, args=("exit",), use_container_width=True)

# Adding new recipe

elif st.session_state.page == "add":
    st.button("⬅ Back to menu", on_click=go_to, args=("home",))
    st.header("Add a new recipe 🥣")

    with st.form("add_recipe_form"):
        category = st.selectbox("Category", ["Breakfast", "Lunch", "Dinner", "Dessert"])
        recipe_name = st.text_input("Recipe name")
        ingredients = st.text_input("Ingredients (comma separated)")
        preptime = st.number_input("Preparation time (minutes)",min_value=1)
        instruction = st.text_area("Cooking instructions")
        difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

        submitted = st.form_submit_button("Save recipe")

    if submitted:
        if not recipe_name.strip() or not ingredients.strip() or not instruction.strip():
            st.error("Check if the recipe name, ingredients and instructions are filled!")
        else:
            rm.save_new_recipe(category, recipe_name, ingredients, int(preptime), instruction, difficulty)
            st.success(f"'{recipe_name}' has been saved!")

#Search by ingredient
elif st.session_state.page == "search":
    st.button("⬅ Back to menu", on_click=go_to, args=("home",))
    st.header("Search recipes by ingredient 🔎📖")

    ingredient = st.text_input("Enter an ingredient")

    if st.button("Search"):
        if not ingredient.strip():
            st.warning("Please enter an ingredient.")
        else:
            results = rm.find_by_ingredient(ingredient)
            if results is None:
                st.error("No recipes file found yet. Add a recipe first.")
            elif results.empty:
                st.info(f"No recipes found with '{ingredient}'.")
            else:
                st.write(f"Recipes containing **'{ingredient}'**:")
                st.dataframe(results, use_container_width=True)

# View all recipes
elif st.session_state.page == "view":
    st.button("⬅ Back to menu", on_click=go_to, args=("home",))
    st.header("All recipes 📖")

    df = rm.view_all()
    if df is None:
        st.error("No recipes file found yet. Add a recipe first.")
    elif df.empty:
        st.warning("No recipes yet. Add one first!")
    else:
        st.dataframe(df, use_container_width=True)

# ---------------- Random recipe ----------------
elif st.session_state.page == "random":
    st.button("⬅ Back to menu", on_click=go_to, args=("home",))
    st.header("Random recipe suggestion")

    if st.button("Give me a recipe!"):
        result = rm.randomizer()
        if result is None:
            st.error("No recipes file found yet. Add a recipe first.")
        else:
            st.dataframe(result, use_container_width=True)

# ---------------- Exit ----------------
elif st.session_state.page == "exit":
    st.title(":wave: Thanks for using Recipe Manager!")
    st.write("You can close this tab now.")
    st.button("⬅ Back to menu", on_click=go_to, args=("home",))