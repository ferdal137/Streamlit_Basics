import streamlit as st
import numpy as np
import pandas as pd

#Slider
x = st.slider('x') #This is a widget

st.write(x,'squared is', x * x)


#Widget keys  (Input of text)
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name


#Checkbox
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

#Selectbox
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
