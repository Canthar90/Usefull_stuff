import streamlit as st

import drink_api



st.set_page_config(
    page_title="Drink",
    page_icon="🍺",   
)

legend = """Pliss keep in mind that 1oz = 29.5735ml
and tsp = teaspoon = 4.92892ml"""

def my_widget(drink_name):
    drink_recipe = drink_api.search_by_name(drink_name)
    st.subheader(drink_recipe["Dring Name"])
    st.image(drink_recipe["Image url"])
    if drink_recipe["Ingredients"]:
        st.write("Nessesary Ingredients:")
        for ingredient in drink_recipe["Ingredients list"]:
            st.write(ingredient)
        
    st.write(drink_recipe["Recipe"])
    st.caption(legend)

st.title("Meet your next drink")
st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)       
st.subheader("Meet random drinks or search for them using ingredients")

with st.expander("Get random drink match"):
    random_drink = st.button(label="Get random drink", key="random_drink_button")
    
with st.expander("Search you new drink"):
    searching_by_name = st.text_input(label="Input drink name", help="Tel me what are you looking for")
    
with st.expander("Find drink by ingredient"):
    searching_by_ingredient = st.text_input(label="Input ingredient", help="Tel me what ingredient you drink should contain")
 
    
if random_drink:
    drin_info = drink_api.random_drink()
    st.subheader(drin_info["Dring Name"])
    st.image(drin_info["Image url"])
    if drin_info["Ingredients"]:
        st.write("Nessesary Ingredients:")
        for ingredient in drin_info["Ingredients list"]:
            st.write(ingredient)
        
    st.write(drin_info["Recipe"])
    st.caption(legend)
    
if searching_by_name:
    try:
        searched_drink = my_widget(searching_by_name.strip())
    except TypeError:
        st.error("You entered invalid drink name.")
                
if searching_by_ingredient:
    try:
        drink_by_ingredients = drink_api.search_by_ingredient(searching_by_ingredient)
        if drink_by_ingredients["end_flag"]:
            st.title("Founded Drinks:")
            for drink in drink_by_ingredients["end_message"]:
                st.subheader(drink[0])
                st.image(f"{drink[1]}", width=100)
                button = st.button(label="Recipe", key=f"drink_{drink[0]}")
                if button:
                    searched_drink = my_widget(drink[0])
        else:
            st.error("You entered invalid ingredient name")
    except IndexError:
        st.error("You entered invalid ingredient name")
        
        
        
st.text("Created by Dawid Cieślak")