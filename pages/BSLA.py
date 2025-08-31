# Liberias
import streamlit as st
import pandas as pd
import plotly.express as px



# set page configuration
st.set_page_config(
    page_title="Dashboard de Incidencias BSMR",
    page_icon=":bar_chart:",
    layout="wide",  
    
)
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    st.image("img/logo_bsmr.png", width=100)

with col3:
    st.image("img/logo1.png", width=100)


#Titulo principal
st.title("Dashboard de Incidencias BSMR")
st.markdown("Análisis de las incidencias reportadas en la planta BSMR durante el mes de febrero de 2025.")

with st.expander("Descripción del Dashboard" , expanded=True):
    st.markdown("""
    Este dashboard presenta un análisis detallado de las incidencias reportadas en la planta BSMR durante el mes de febrero de 2024. 
    Incluye gráficos y tablas que muestran la distribución de las incidencias por categoría, nivel de gravedad y área afectada.
    """)

# Cargar los datos desde el archivo CSV
try:
    incidencias_df = pd.read_csv('data/03_formateado.csv')
    #st.success("Datos cargados correctamente desde 'incidencias_febrero.csv'.")
    
    
    st.header("Datos de Incidencias")
    with st.container():
        # Graficar los primeros registros del DataFrame
        fig = px.bar(
            incidencias_df,
            x='Categoría',
            y='Cantidad',
            title='Cantidad de Incidencias por Categoría',
            labels={
                'Cantidad': 'Cantidad de Incidencias',
                'Categoría': 'Categoría'
            },
            color='Nivel'
        )
        st.plotly_chart(fig, use_container_width=True)

        
        # Grafica de Pastel 
        fig= px.pie(incidencias_df,
                    values= "Cantidad",
                    names="Categoría",
                    title= "Grado de incidencias")
        st.plotly_chart(fig,use_container_width=True)

        st.title('Visualización de datos')
        st.dataframe(incidencias_df)    
        

        suma = incidencias_df['Cantidad'].sum()
        st.write(f"La suma de la columna es: {suma}")
    
except Exception as e:
    st.success(f"Error al cargar los datos: {e}")
    
