import streamlit as st
import pandas as pd
import json

st.title("My First Deployed App 🚀")
st.write("Hello from Streamlit Community Cloud!")


with open('data.json') as f:
    data=json.load(f)

df= pd.DataFrame(data) 

st.dataframe(df)
