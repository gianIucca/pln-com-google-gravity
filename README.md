# Sistema de classificação automática de textos financeiros desenvolvido com técnicas de Processamento de Linguagem Natural (NLP) e Machine Learning. O modelo classifica notícias e artigos financeiros em 11 categorias distintas, utilizando TF-IDF para extração de features e Random Forest para classificação. <br>
## Categorias de Classificação <br>
O sistema identifica automaticamente as seguintes categorias financeiras: <br>

International_Finance - Finanças Internacionais <br>
Earning_Reports - Relatórios de Resultados <br>
Commodities - Mercado de Commodities <br>
Economy - Economia Geral <br>
Fraud - Fraudes Financeiras <br>
Mergers_Acquisitions - Fusões e Aquisições <br>
Policy - Políticas Econômicas <br>
Oil - Mercado Petrolífero <br>
Capital - Mercado de Capitais <br>
Litigation - Litígios Financeiros <br>
Real_Estate - Mercado Imobiliário <br>

## Arquitetura Técnica <br>

Processamento de Dados: pandas <br>
NLP: TfidfVectorizer (scikit-learn) <br>
Machine Learning: RandomForestClassifier <br>
Serialização: pickle <br>
Deploy: gravityai <br>

# Pipeline de Processamento <br>

## Pré-processamento de Texto <br>

Remoção de stop words em inglês <br>
Vetorização TF-IDF com limite de 1000 features <br>
Transformação para lowercase automática <br>


## Engenharia de Features <br>

Label encoding para categorias <br>
Vetorização TF-IDF do corpo do texto <br>
Normalização automática dos dados <br>


## Treinamento do Modelo <br>

Random Forest Classifier para classificação multi-classe <br>
Treinamento com 8042 amostras de dados <br>
Serialização dos modelos treinados <br>


## Casos de Uso <br>

Automação de Newsroom: Categorização automática de notícias financeiras <br> 
Análise de Sentimento Setorial: Classificação de conteúdo por setor financeiro <br>
Curadoria de Conteúdo: Organização automática de feeds financeiros <br>
Compliance: Identificação automática de conteúdo de risco (fraudes, litígios) <br>

<br>

Tecnologias: Python, Scikit-learn, Pandas, TF-IDF, Random Forest, Pickle <br>
Competências: NLP, Machine Learning, Text Classification, Data Engineering, Model Deployment
