import yfinance as yf
import streamlit as st
st.title("stock dashboard")

tab1,tab2,tab3=st.tabs(["Overview","Price chart","Price"])

comp = st.text_input("Enter stock ticker",value="AAPL").upper()
# filtering the date for a compnay name entered by the user in comp
data = yf.Ticker(comp)
df = data.history(start="2019-01-01", end="2023-01-01")

# filering of dataframe ends here

# In overview tabs we are going to showcase
with tab1:
    st.header("Stock overview")
    st.dataframe(df)


with tab2:
    st.subheader("Closing Price chart")
    st.line_chart(df["Close"])

with tab3: 
     st.subheader("Volumn chart")
     st.bar_chart(df["Volume"])