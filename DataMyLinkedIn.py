# pandas = Library for load and handling of data
# random and string = Library to generate random strings
# Graphic libraries = matplotlib, seaborn amd wordcloud to graphics

import pandas as pd
import random, string
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv('Connections.csv')

df.isna().sum()

# GPDR / LDPG requirement, keeping sensible data hidden
assert isinstance(df, object)
df.drop(['First Name', 'Last Name', 'Email Address'], inplace=True, axis=1, errors = 'ignore')
df.head()

# Adding random ID column
df.reset_index(inplace=True)
df.rename(columns={'index':'id'}, inplace=True)

# Fuction ID = 8 charecters
def get_id():
  id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
  return id

# Setting ID with get_id function
for r in range(df.shape[0]):
  df[id].iloc._setitem_with_indexer(r, get_id())

#Total of connections
df.shape[0]

#Connections by organization
df['Company'].value_counts()

# Changing everything to UPPERCASE
df = df.apply(lambda x: x.astype(str).str.upper())
# Removing punctuation
df['Position'] = df['Position'].str.replace('[,.:;!?]+', '', regex=True).copy()
# Reming special characters
df['Position'] = df['Position'].str.replace('[/<>()|\+\-\–$%&#@\'\"]+', '', regex=True).copy()
# Removendo double space
df['Position'] = df['Position'].str.replace('  ', ' ', regex=True).copy()

#Function that modifies the postion based on a precisely string
def change_position(position,new_position):
  df['Position'].iloc[df.query('Position == @position').index] = new_position
#Function that modifies the position the "contain" the string
def change_area_full(position,new_position):
  df['Position'].iloc[df.query('Position.str.contains(@position)', engine='python').index]

change_area_full('QUALIDADE'        ,'QUALITY')
change_area_full('SGI'         ,'QUALITY')
change_area_full('SGQ'    ,'QUALITY')
change_area_full('MEIO AMBIENTE'    ,'ENVIRONMENT')
change_area_full('ISO'    ,'QUALITY')

# Creating column, day, month and year starting from of Connected On
df['Connected Day'] = df['Connected On'].dt.day
df['Connected Month'] = df['Connected On'].dt.month
df['Connected Year'] = df['Connected On'].dt.year
df['Connected YearMonth'] = df['Connected Year'].apply(str) + df['Connected Month'].apply(str).apply(lambda x: x.zfill(2))

#Setting charts parameters
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (20,10)
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['font.size'] = 15
plt.rcParams['axes.titlesize'] = 20

#Chart top 10 roles of connections
x = df['Position'].value_counts().head(10).values
y = df['Position'].value_counts().head(10).index
sns.barplot(x=x, y=y)
plt.title('Top 10 Cargos das Conexões')
plt.show()

#Evolution of number of connections thru time
YearMonth = pd.DataFrame(pd.DataFrame(df['Connected YearMonth'].value_counts())).rename(columns={'Connected YearMonth': 'Conexões'}).sort_index()
# Gráfico de linha com evolução das conexões
sns.lineplot(data=YearMonth,
            palette="tab10",
            linewidth=2.5,
            estimator='sum')
plt.title('Como foi a evolução das suas conexões no LinkedIn?')
plt.xlabel('AnoMês')
plt.xticks(rotation = 60)
plt.ylabel('Quantidade')
plt.show()

#Chart quantity of connections by month
x = df['Connected Month'].value_counts().index
y = df['Connected Month'].value_counts().values
sns.barplot(x=x, y=y)
plt.title('Quantidade de Conexões por Mês')
plt.show()

#Chart quantity of connections by year
x = df['Connected Year'].value_counts().index
y = df['Connected Year'].value_counts().values
sns.barplot(x=x, y=y)
plt.title('Quantidade de Conexões por Ano')
plt.show()

#Plotting wordcloud - Removing connector
todos_itens = ' '.join(s for s in df['Position'].values)
stop_words = ['sem', 'cargo', 'de', 'da', 'do', 'and', 'e', 'in']
 
#Creating the wordcloud
wc = WordCloud(stopwords=stop_words, background_color="black", width=1600, height=800)
wordcloud = wc.generate(todos_itens)
 
#Print the wordcloud
fig, ax = plt.subplots(figsize=(15,9))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
