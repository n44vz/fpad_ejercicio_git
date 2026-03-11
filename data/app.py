import streamlit as st
import pandas as pd

# Configuración básica
st.set_page_config(page_title="Dashboard Ventas", layout="wide")

# Función de carga de datos
@st.cache_data
def load_data():
    return pd.read_csv('data/ventas.csv')

df = load_data()

st.title("Reporte de Ventas")
st.write("Datos cargados exitosamente:")
st.dataframe(df.head())

st.markdown("---")

# Funcionalidad A: Filtros por Sucursal
st.sidebar.header("Filtros")
sucursal = st.sidebar.selectbox("Seleccionar Sucursal", df['sucursal'].unique())

df_filtered = df[df['sucursal'] == sucursal]
st.subheader(f"Ventas de la sucursal: {sucursal}")
st.bar_chart(df_filtered.set_index('producto')['ingreso'])