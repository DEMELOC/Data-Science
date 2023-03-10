# pandas = Library for handling and treatment of data
# random and string = Library to generate random strings
# Graphic libraries = matplotlib, seaborn amd wordcloud to graphics

import pandas as pd
import random, string
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

#Import the file to the python array to a function that can be used within the code

df_file = pd.read_csv('Connections.csv')
df_file.info()
input("Press Enter to continue")

# For follow into the GPDR / LDPG requirement, keeping sensible data is elimnated
assert isinstance(df_file, object)
df_file.drop(['First Name', 'Last Name', 'Email Address'], inplace=True, axis=1)
print(df_file)
input("Press Enter to continue")

# Adding a new column labeled id for index usage
df_file.reset_index(inplace=True)
df_file.rename(columns={'index':'Number'}, inplace=True)
print(df_file)
input("Press Enter to continue")

# Fuction to create a randomic id number with 8 characteres
def get_id():
  Number = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for r in range(8))
  return Number

# Setting the id numbers with get_id fuction
for r in range(df_file.shape[0]):
  df_file['Number'].iloc._setitem_with_indexer(r, get_id())
print(df_file)
input("Press Enter to continue")

#Total of connections by organization
byorg = df_file['Company'].value_counts()
print(byorg)
input("Press Enter to continue")

#Total of connections by position
byrole = df_file['Position'].value_counts()
print(byrole)
input("Press Enter to continue")

#Total of connections by date of connection
bydate = df_file['Position'].value_counts()
print(bydate)
input("Press Enter to continue")
