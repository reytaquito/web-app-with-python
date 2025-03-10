import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('/Users/rodrigomateos/Desktop/Python Notebooks/web-app-with-python/vehicles_us.csv')
hist_button = st.button('Construir histograma') # crear un botón
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)