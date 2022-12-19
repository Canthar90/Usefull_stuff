import streamlit as st
import sys

sys.path.insert(1, ".\\")

import drink_api

st.title("Simple app to meet your next drink")
    

with st.expander("Random drink"):
    random_drink = st.button(label="Get random drink", key="random_drink_button")
    
    
if random_drink:
    drin_info = drink_api.random_drink()
    st.subheader(drin_info["Dring Name"])
    st.image(drin_info["Image url"])
    st.write(drin_info["Description"])
    