import langchain_helper as lh
import streamlit as st

st.title("Pets")

animal = st.text_input("What kind of pet do you have?: ", max_chars = 10)
breed = st.text_input("Please enter the breed: ", max_chars = 10)
color = st.text_input("Please enter the color of your pet: ", max_chars = 10)

if st.button("Get names"):
  response = lh.get_pet_name(animal, breed, color)
  st.text(response)