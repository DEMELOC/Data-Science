# pandas = Library for load and handling of data
# random and string = Library to generate random strings
# Graphic libraries = matplotlib, seaborn amd wordcloud to graphics

import pandas as pd
import random, string
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df_file = pd.read_csv('Connections.csv')
df_file.info()
input("Press Enter to continue")

# GPDR / LDPG requirement, keeping sensible data hidden
assert isinstance(df_file, object)
df_file.drop(['First Name', 'Last Name', 'Email Address'], inplace=True, axis=1)
print(df_file)
input("Press Enter to continue")

# Adding random id number column
df_file.reset_index(inplace=True)
df_file.rename(columns={'index':'Number'}, inplace=True)
print(df_file)
input("Press Enter to continue")

# Fuction to create a randomic id number with 8 characteres
def get_id():
  Number = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for r in range(8))
  return Number
print(df_file)
input("Press Enter to continue")

# Setting the id numbers with get_id fuction
for r in range(df_file.shape[0]):
  df_file['Number'].iloc._setitem_with_indexer(r, get_id())

#Checking total number of connections
df_file.shape[0]
input("Press Enter to continue")

df_file.head()
