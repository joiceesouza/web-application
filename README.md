# Gerador de Gráficos com Streamlit

Este projeto usa **Streamlit** e **Plotly** para gerar gráficos interativos a partir de um conjunto de dados sobre vendas de carros.

## 📌 Requisitos
Certifique-se de ter o **Python** instalado e, em seguida, instale as bibliotecas necessárias:
```sh
pip install streamlit pandas plotly
```

## 🚀 Como Executar

**1.** Clone este repositório:
```
git clone https://github.com/joiceesouza/web-application.git
cd seu-repositorio
```
 **2. Execute o Streamlit:**
 ```
 streamlit run app.py
 ```

**3. Abra no navegador o endereço indicado, como http://localhost:10000**

**4.** <a href="https://web-application-c6rq.onrender.com" target="_blank">Ou clique aqui </a>


## 📊 Funcionalidades

- **Criar Histograma**: Mostra a distribuição de valores da coluna odometer.

- **Criar Gráfico de Dispersão**: Relaciona model e price.

## 🗂 Estrutura do Projeto
```
/WEB-APPLICATION
│-- .streamlit/
│   ├── config.toml  # Configuração do Streamlit
│-- data/
│   ├── vehicles.csv  # Conjunto de dados
│-- notebooks/
│   ├── EDA.ipynb  # Jupyter Notebook
│-- app.py  # Código principal
│-- README.md  # Documentação
│-- requirements.txt  # Código com bibliotecas
```

## 🔧 Possíveis Erros
Arquivo de dados não encontrado: Verifique se vehicles.csv está no diretório correto (data/vehicles.csv).

Porta em uso: Se o Streamlit não iniciar, tente mudar a porta com:
``` streamlit run app.py --server.port 8502 ```



