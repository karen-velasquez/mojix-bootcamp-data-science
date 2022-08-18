import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.write("HELLO MOJIX")
file =  st.file_uploader('upload a csv', type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df)
    st.markdown("---")
    fig1 = plt.figure(figsize=(10,4))
    sns.countplot(x='Pclass',data=df)
    
    st.pyplot(fig1)
    fig2 = plt.figure(figsize=(10,4))