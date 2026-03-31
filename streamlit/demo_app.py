import streamlit as st

st.title("Welcom to this demo app")
st.header("This is a car price prediction app")
st.subheader("Please enter the details of your car to get prdiction")
# Checkbox help user to interact with app
if st.checkbox("show/hide"): # Widget is somthing that alwasy users to interact
    # Main component of streamlit is widget
    st.text("this is simple app to showcasw streamlit features for prediction of car")

if st.button("click here for more infor"):
    st.text("this is a car price app")
