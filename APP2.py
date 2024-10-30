import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
st.title('More charts and utilities')
data = pd.read_csv('https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/refs/heads/main/data/penguins.csv')
st.sidebar.header('Select options')
selected_category = st.sidebar.selectbox('Select Spicies', options=['All', 'Adele', 'Gentoo', 'Chinstrap'])
if selected_category != 'All':
    filtered_data = data[data['species' == selected_category]]
else:
    filtered_data = data
st.write('###matplotlib histogram')
fig, ax = plt.subplots()
ax.hist(filtered_data['culmen_length_mm'], bins=30, color='skyblue', edgecolor='black')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
st.pyplot(fig)

st.write('###Seaborn Density Plot')
fig, ax = plt.subplots()
fig = sns.displot(filtered_data['culmen_depth_mm'], color='black', kind='kde', ax= ax, fill=True)
ax.set_title('Seaborn Desity plot for culmen Depths')
ax.set_xlabel('Value')
ax.set_ylabel('density')
st.pyplot(fig)

st.write('altair Scatter Plot')

scatter_plot = alt.Chart(filtered_data).mark_circle().encode(
    x=alt.X('flipper_length_mm', title='Flipper Length'),
    y=alt.Y('body_mass_g', title='Body Mass'),
    color=alt.Color('island', scale=alt.Scale(scheme='tableau10')),
    tooltip=['island', 'flipper_length_mm', 'body_mass_g']
).properties(
    width=600,
    height=400,
    title='Scatter Plot of Penguins Data'
).interactive()
st.altair_chart(scatter_plot, use_container_width=True)