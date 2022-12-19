import streamlit as st

import drink_api


st.set_page_config(
    page_title="Drink",
    page_icon="🍺",
)

st.title("Meet your next drink")
    
st.subheader("Meet random drinks or search for them using ingredients")

with st.expander("Get random drink match"):
    random_drink = st.button(label="Get random drink", key="random_drink_button")
    
with st.expander("Search you new drink"):
    searching_by_name = st.text_input(label="Input drink name", help="Tel me what are you looking for")
    
    
if random_drink:
    drin_info = drink_api.random_drink()
    st.subheader(drin_info["Dring Name"])
    st.image(drin_info["Image url"])
    st.write(drin_info["Description"])
    
if searching_by_name:
    try:
        searched_drink = drink_api.search_by_name(searching_by_name)
        st.subheader(searched_drink["Dring Name"])
        st.image(searched_drink["Image url"])
        st.write(searched_drink["Description"])
    except TypeError:
        st.error("You entered invalid drink name.")