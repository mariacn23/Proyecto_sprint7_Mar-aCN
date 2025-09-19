import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Vehículos", layout="wide")
st.header("Análisis de anuncios de venta de coches")

# --- Cargar datos ---
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

DATAFILE = "vehicles_us.csv"
car_data = load_data(DATAFILE)

# Mensaje rápido con info del dataset
st.write(f"Filas: {car_data.shape[0]:,} · Columnas: {car_data.shape[1]}")

# --- Botones requeridos ---
col1, col2 = st.columns(2)

with col1:
    hist_button = st.button("Construir histograma (odometer)")

with col2:
    scatter_button = st.button("Construir dispersión (price vs odometer)")

# Histograma
if hist_button:
    st.write("Creación de un histograma para la columna **odometer**")
    fig = go.Figure(data=[go.Histogram(x=car_data["odometer"])])
    fig.update_layout(title_text="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

# Dispersión
if scatter_button:
    st.write("Gráfico de dispersión **price vs odometer**")
    fig2 = go.Figure(
        data=[go.Scatter(
            x=car_data["odometer"],
            y=car_data["price"],
            mode="markers",
            opacity=0.6
        )]
    )
    fig2.update_layout(title_text="Precio vs Odómetro")
    st.plotly_chart(fig2, use_container_width=True)

# (Opcional) versión con casillas de verificación
with st.expander("Usar casillas de verificación (opcional)"):
    show_hist = st.checkbox("Histograma de odometer")
    show_scatter = st.checkbox("Dispersión price vs odometer")
    if show_hist:
        fig_h = go.Figure([go.Histogram(x=car_data["odometer"])])
        st.plotly_chart(fig_h, use_container_width=True)
    if show_scatter:
        fig_s = go.Figure([go.Scatter(x=car_data["odometer"], y=car_data["price"], mode="markers", opacity=0.6)])
        st.plotly_chart(fig_s, use_container_width=True)