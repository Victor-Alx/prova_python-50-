import pandas as pd
import openpyxl
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="PIB Real do Brasil", layout="wide")
st.title("PIB Real do Brasil")
st.header("Visualização dos Dados em Tabela e Gráfico")

df = pd.read_excel("pib.xlsx")
df["ano"] = df["Data"].astype(str).str[:4]
media = df.groupby("ano")["PIB real"].mean().reset_index()

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.header("Tabela do PIB Real")
    st.dataframe(df, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.header("Gráficos do PIB Real")
    st.subheader("Gráfico de Linha ")

    fig_linha_PIB = px.line(
        df,
        x="ano",
        y="PIB real",
        markers=True,
        title="Média de PIB por Ano",
        template="plotly_dark"
    )
    fig_linha_PIB.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
    fig_linha_PIB.update_xaxes(type="category")
    fig_linha_PIB.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_linha_PIB, use_container_width=True)
    
st.caption("Fonte dos dados: IPEA, http://www.ipeadata.gov.br/")