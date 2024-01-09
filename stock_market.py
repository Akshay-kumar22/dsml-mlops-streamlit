import streamlit as st
import yfinance as yf 
import pandas as pd 


st.title("Stock market App")
user_input=st.text_input("Enter the stock name","MSFT")
ticker_symbol=user_input

msft = yf.Ticker(ticker_symbol)

hist = msft.history(start="2022-05-31",end="2022-07-30")

st.write(hist)