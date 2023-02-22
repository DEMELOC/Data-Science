# pandas = Library for load and handling of data
# random and string = Library to generate random strings
# Graphic libraries = matplotlib, seaborn amd wordcloud to graphics

import pandas as pd
import random, string
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv('Connections.csv')
df.info()
input("Press Enter to continue")

# GPDR / LDPG requirement, keeping sensible data hidden
assert isinstance(df, object)
df.drop(['First Name', 'Last Name', 'Email Address'], inplace=True, axis=1, errors = 'ignore')
df.head()
df.info()
input("Press Enter to continue")

# Adding random ID column
df.reset_index(inplace=True)
df.rename(columns={'index':'id'}, inplace=True)
df.info()
input("Press Enter to continue")
