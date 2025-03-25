import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.io as pio

pio.renderers.default = 'browser'
car_data = pd.read_csv('data/vehicles.csv') # lendo os dados
st.header('Clique no botão para gerar um histograma')
hist_button = st.button('Criar histograma') # criar um botão
px_button = st.button('Criar um gráfico de dispersão')

try:      
    if hist_button: # se o botão for clicado
                # escrever uma mensagem
        st.write('#### Criando um histograma para o conjunto de dados de anúncios de vendas de carros...')
                
                # criar um histograma
        fig = px.histogram(car_data, x="odometer")
            
                # exibir um gráfico Plotly interativo
        st.plotly_chart(fig, use_container_width=True)

    elif px_button:
        st.write("#### Criando um gráfico de dispersão para um conjunto de dados de anúncio de vendas de carros..")
        fig = px.scatter(car_data,x="model", y="price", title="Gráfico de Dispersão")
        st.write("### Gráfico de Dispersão Gerado")
        st.plotly_chart(fig)
        
except FileNotFoundError:
    st.error("Erro: Conjunto de dados não encontrado. Verifique se o arquivo 'car_data.csv' está no diretório correto.")
except Exception as e:
    st.error(f"Ocorreu um erro inesperado: {e}")
    