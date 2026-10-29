import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Anuncios de venta de coches')

build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Histograma de la columna odómetro')
    fig = px.histogram(car_data, x='odometer', title='Distribución del odómetro')
    st.plotly_chart(fig, width='stretch')

build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Gráfico de dispersión: precio vs. odómetro')
    fig = px.scatter(car_data, x='odometer', y='price', title='Precio vs. odómetro')
    st.plotly_chart(fig, width='stretch')