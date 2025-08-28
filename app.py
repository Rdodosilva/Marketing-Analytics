import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuração da página
st.set_page_config(
    page_title="Marketing Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para visual futurista
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stMetric {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 10px;
        backdrop-filter: blur(10px);
    }
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
    }
    h1, h2, h3 {
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .stDataFrame {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Função para carregar dados
@st.cache_data
def load_data():
    df = pd.read_csv("marketing_data.csv")
    df['Data'] = pd.to_datetime(df['Data'])
    return df

# Função para criar gráficos com gradientes
def create_gradient_bar_chart(data, x_col, y_col, title, color_scheme='viridis'):
    fig = px.bar(
        data, 
        x=x_col, 
        y=y_col,
        title=title,
        color=y_col,
        color_continuous_scale=color_scheme,
        template='plotly_dark'
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        title_font_size=20,
        showlegend=False
    )
    return fig

def create_gradient_line_chart(data, x_col, y_col, title, color_scheme='plasma'):
    fig = px.line(
        data, 
        x=x_col, 
        y=y_col,
        title=title,
        template='plotly_dark'
    )
    fig.update_traces(
        line=dict(width=3, color='rgba(255,255,255,0.8)'),
        fill='tonexty',
        fillcolor='rgba(255,255,255,0.1)'
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        title_font_size=20
    )
    return fig

# Carregar dados
df = load_data()

# Título principal
st.title("🚀 Marketing Analytics Dashboard")
st.markdown("### Análise Futurista de Performance de Marketing")

# Sidebar para filtros
st.sidebar.header("🎛️ Filtros")
campanhas_selecionadas = st.sidebar.multiselect(
    "Selecione as Campanhas:",
    options=df['Campanha'].unique(),
    default=df['Campanha'].unique()
)

canais_selecionados = st.sidebar.multiselect(
    "Selecione os Canais:",
    options=df['Canal'].unique(),
    default=df['Canal'].unique()
)

# Filtrar dados
df_filtrado = df[
    (df['Campanha'].isin(campanhas_selecionadas)) &
    (df['Canal'].isin(canais_selecionados))
]

# Métricas principais
col1, col2, col3, col4 = st.columns(4)

with col1:
    receita_total = df_filtrado['Receita'].sum()
    st.metric("💰 Receita Total", f"R$ {receita_total:,.2f}")

with col2:
    roi_medio = df_filtrado['Retorno_Sobre_Investimento'].mean()
    st.metric("📈 ROI Médio", f"{roi_medio:.2f}%")

with col3:
    conversoes_total = df_filtrado['Conversoes'].sum()
    st.metric("🎯 Conversões Total", f"{conversoes_total:,}")

with col4:
    ctr_medio = df_filtrado['Taxa_Cliques'].mean()
    st.metric("👆 CTR Médio", f"{ctr_medio:.2f}%")

# Gráficos principais
col1, col2 = st.columns(2)

with col1:
    # Receita por Campanha
    receita_campanha = df_filtrado.groupby('Campanha')['Receita'].sum().reset_index()
    receita_campanha = receita_campanha.sort_values('Receita', ascending=False)
    
    fig1 = create_gradient_bar_chart(
        receita_campanha, 
        'Campanha', 
        'Receita', 
        '💎 Receita por Campanha',
        'viridis'
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # ROI por Canal
    roi_canal = df_filtrado.groupby('Canal')['Retorno_Sobre_Investimento'].mean().reset_index()
    roi_canal = roi_canal.sort_values('Retorno_Sobre_Investimento', ascending=False)
    
    fig2 = create_gradient_bar_chart(
        roi_canal, 
        'Canal', 
        'Retorno_Sobre_Investimento', 
        '🔥 ROI Médio por Canal',
        'plasma'
    )
    st.plotly_chart(fig2, use_container_width=True)

# Tendência temporal
st.subheader("📅 Tendência de Performance ao Longo do Tempo")

# Agrupar por data
tendencia_diaria = df_filtrado.groupby('Data').agg({
    'Receita': 'sum',
    'Conversoes': 'sum',
    'Retorno_Sobre_Investimento': 'mean'
}).reset_index()

fig3 = create_gradient_line_chart(
    tendencia_diaria,
    'Data',
    'Receita',
    '💹 Evolução da Receita Diária'
)
st.plotly_chart(fig3, use_container_width=True)

# Análise por segmento
col1, col2 = st.columns(2)

with col1:
    # Performance por Segmento
    segmento_performance = df_filtrado.groupby('Segmento_Alvo').agg({
        'Receita': 'sum',
        'Conversoes': 'sum',
        'Retorno_Sobre_Investimento': 'mean'
    }).reset_index()
    
    fig4 = px.scatter(
        segmento_performance,
        x='Conversoes',
        y='Receita',
        size='Retorno_Sobre_Investimento',
        color='Segmento_Alvo',
        title='🎯 Performance por Segmento de Público',
        template='plotly_dark',
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    fig4.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    # Custo vs Receita por Região
    regiao_performance = df_filtrado.groupby('Regiao').agg({
        'Custo': 'sum',
        'Receita': 'sum'
    }).reset_index()
    regiao_performance['Lucro'] = regiao_performance['Receita'] - regiao_performance['Custo']
    
    fig5 = px.bar(
        regiao_performance,
        x='Regiao',
        y=['Custo', 'Receita'],
        title='💰 Custo vs Receita por Região',
        template='plotly_dark',
        color_discrete_sequence=['#ff6b6b', '#4ecdc4']
    )
    fig5.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )
    st.plotly_chart(fig5, use_container_width=True)

# Tabela de dados detalhados
st.subheader("📋 Dados Detalhados")
st.dataframe(
    df_filtrado.style.background_gradient(cmap='viridis'),
    use_container_width=True
)

# Insights automáticos
st.subheader("🧠 Insights Automáticos")

melhor_campanha = df_filtrado.groupby('Campanha')['Receita'].sum().idxmax()
melhor_canal = df_filtrado.groupby('Canal')['Retorno_Sobre_Investimento'].mean().idxmax()
melhor_segmento = df_filtrado.groupby('Segmento_Alvo')['Conversoes'].sum().idxmax()

col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"🏆 **Melhor Campanha:** {melhor_campanha}")

with col2:
    st.info(f"🚀 **Melhor Canal (ROI):** {melhor_canal}")

with col3:
    st.info(f"🎯 **Melhor Segmento:** {melhor_segmento}")

# Footer
st.markdown("---")
st.markdown("### 🔮 Dashboard criado com tecnologia futurista para análise de marketing")

