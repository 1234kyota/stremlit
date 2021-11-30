import streamlit as st
import numpy as np
import pandas as pd


st.title("Streamlit超入門")

st.write("インターラクティブなウィジェット")

left_column,right_column = st.columns(2)
button = left_column.button("右")
if button:
    right_column.write("data")

# text = st.sidebar.text_input("あなたの趣味を教えてください")
# condition = st.sidebar.slider("調子",0,100,50)

# "あなたの趣味",text
# "コンディション",condition


# if st.checkbox("show image"):
#     img = Image.open("125bfb59d894ffeca879098a9bbf4394.jpeg")
#     st.image(img,caption="FF",use_column_width=True)



