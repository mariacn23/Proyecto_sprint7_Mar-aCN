# Proyecto_sprint7_Mar-aCN

# Proyecto Sprint 7 — Panel web con Streamlit (Vehículos US)

Aplicación web simple hecha con **Streamlit** para visualizar un dataset de anuncios de venta de autos.  
Incluye un **histograma** (odometer) y un **gráfico de dispersión** (price vs odometer), controlados por **botones** y/o **casillas de verificación**.

## Demo
- **URL (Render):** <https://proyecto-sprint7-mariacn.onrender.com>

## Funcionalidad
- Encabezado con el título.
- Botón para **histograma** de `odometer`.
- Botón para **dispersión** `price` vs `odometer`.
- (Opcional) casillas para mostrar/ocultar gráficos.

## Cómo ejecutar en local
```bash
conda activate vehicles_env
streamlit run app.py