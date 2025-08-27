# 🚀 Marketing Analytics Dashboard

Um dashboard futurista e interativo para análise de dados de marketing, desenvolvido com Streamlit e visualizações com gradientes translúcidos.

## 📊 Sobre o Projeto

Este projeto foi desenvolvido para demonstrar habilidades em análise de dados de marketing, criando um dashboard moderno e atraente que oferece insights valiosos sobre performance de campanhas, canais e segmentos de público.

## ✨ Características

- **Design Futurista**: Interface com gradientes, cores translúcidas e efeitos visuais modernos
- **Análise Interativa**: Filtros dinâmicos por campanha e canal
- **Métricas Principais**: ROI, receita, conversões e CTR
- **Visualizações Avançadas**: Gráficos com gradientes usando Plotly
- **Insights Automáticos**: Identificação automática dos melhores performers

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Streamlit** - Framework para aplicações web
- **Pandas** - Manipulação e análise de dados
- **Plotly** - Visualizações interativas
- **Matplotlib & Seaborn** - Gráficos estáticos
- **NumPy** - Computação numérica

## 📁 Estrutura do Projeto

```
marketing-analytics/
├── marketing_dashboard.py    # Aplicação principal Streamlit
├── marketing_data.csv       # Dataset de marketing
├── requirements.txt         # Dependências do projeto
├── insights.md             # Insights da análise exploratória
├── generate_plots.py       # Script para gerar visualizações
└── README.md              # Documentação do projeto
```

## 🚀 Como Executar

1. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

2. **Executar o dashboard:**
```bash
streamlit run marketing_dashboard.py
```

3. **Acessar no navegador:**
```
http://localhost:8501
```

## 📈 Funcionalidades do Dashboard

### Métricas Principais
- **Receita Total**: Soma de toda receita gerada
- **ROI Médio**: Retorno sobre investimento médio
- **Conversões Total**: Total de conversões obtidas
- **CTR Médio**: Taxa de cliques média

### Visualizações
1. **Receita por Campanha**: Gráfico de barras com gradiente viridis
2. **ROI por Canal**: Gráfico de barras com gradiente plasma
3. **Tendência Temporal**: Evolução da receita ao longo do tempo
4. **Performance por Segmento**: Scatter plot com tamanho baseado no ROI
5. **Custo vs Receita por Região**: Comparação de custos e receitas

### Filtros Interativos
- Seleção múltipla de campanhas
- Seleção múltipla de canais
- Atualização automática de todos os gráficos

## 🎨 Design e Estilo

O dashboard utiliza:
- **Gradientes**: Cores que transitam suavemente
- **Transparências**: Elementos com efeito glass morphism
- **Tema Escuro**: Background escuro para contraste
- **Cores Vibrantes**: Paletas modernas (viridis, plasma, magma)
- **Tipografia**: Emojis e ícones para melhor UX

## 📊 Insights Gerados

O dashboard identifica automaticamente:
- Melhor campanha por receita
- Melhor canal por ROI
- Melhor segmento por conversões
- Tendências temporais de performance

## 🔧 Personalização

Para adaptar o dashboard aos seus dados:

1. **Substitua o arquivo CSV** com seus dados de marketing
2. **Ajuste as colunas** no código conforme necessário
3. **Modifique as cores** alterando as paletas nos gráficos
4. **Adicione novas métricas** seguindo o padrão existente

## 📱 Responsividade

O dashboard é totalmente responsivo e funciona em:
- Desktop
- Tablet
- Mobile

## 🚀 Deploy

Para fazer deploy do dashboard:

### Streamlit Cloud
1. Faça upload do projeto no GitHub
2. Conecte com Streamlit Cloud
3. Configure as dependências
4. Deploy automático

### Heroku
1. Adicione `Procfile` com: `web: streamlit run marketing_dashboard.py --server.port=$PORT --server.address=0.0.0.0`
2. Configure buildpack Python
3. Deploy via Git

## 📈 Próximas Melhorias

- [ ] Integração com APIs de marketing (Google Ads, Facebook Ads)
- [ ] Previsões com Machine Learning
- [ ] Exportação de relatórios em PDF
- [ ] Alertas automáticos de performance
- [ ] Dashboard em tempo real

## 👨‍💻 Autor

Desenvolvido como projeto de portfólio para demonstrar habilidades em:
- Análise de dados de marketing
- Desenvolvimento de dashboards interativos
- Visualização de dados moderna
- Python e Streamlit

---

**🔮 Dashboard criado com tecnologia futurista para análise de marketing**

