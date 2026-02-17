import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(page_title="Dashboard Ventas", layout="wide")

# Carga de datos
def load_data():
    return pd.read_csv('data/ventas.csv')

df = load_data()

st.title("📊 Reporte de Ventas")
st.write("Datos crudos del sistema:", df)

# --- ZONA DE CONFLICTO ---
# Zona para agregar conflictos distintos
# -------------------------
