import streamlit as st
import pandas as pd
from sklearn import datasets
st.write("""
# find the largest number
This app gives the largest number from your input

""")

st.header("Input parameter")

input_1 = st.number_input("Enter first number")
input_2 = st.number_input("Enter second number")
input_3 = st.number_input("Enter third number")
l = [input_1, input_2, input_3]
ans = max(l)
data = {"First Number": input_1,
        "Second Number": input_2,
        "Third Number": input_3
       }  
features = pd.DataFrame(data, index=[0])
features 
st.subheader("user input parameter")
data
st.subheader("Largest number among the inputs")
ans
