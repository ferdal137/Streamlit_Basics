import streamlit as st
import pandas as pd
import numpy as np

st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
	'first column': [1,2,3,4],
	'second column': [10,20,30,40,]
})

st.write("With pandas:")
df

df_numpy = np.random.randn(10,20)

st.write("With numpy:")
st.dataframe(df_numpy)

dataframe = pd.DataFrame(
	np.random.randn(10,20),
	columns = ('col %d' % i for i in range(20)))

st.write("Pandas styler:")
st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("Static Table:")
st.table(dataframe)

st.write("Draw a line chart: ")
chart_data = pd.DataFrame(
		np.random.randn(20,3),
		columns=['a','b','c'])

st.line_chart(chart_data)

st.write("Plot a map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)