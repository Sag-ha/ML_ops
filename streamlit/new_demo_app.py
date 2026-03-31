import streamlit as st

st.title("Welcom to this demo app")

st.header("This is a car price prediction app")

def sqr(num):
    return num*num

num=st.number_input("Insert a number from the user", value=0) # If user does not enter any anything it take 0

if st.button("sumbit"):
    result=sqr(num)
    st.write(f"The square of {num} is {result}")