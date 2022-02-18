# Modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")
plt.scatter(df['Weight'], df['Height'], c=df.Index )
#plt.show()

plt.figure(figsize=(15,8))
sns.scatterplot(x='Weight', y='Height', hue='Index', data=df ,palette="deep")
plt.show()