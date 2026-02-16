import streamlit as st
import pandas as pd

st.title("My First Deployed App 🚀")
st.write("Hello from Streamlit Community Cloud!")


with open('data.json') as f:
    data=json.load(f)

df= pd.Dataframe(data) 

st.dataframe(df)
