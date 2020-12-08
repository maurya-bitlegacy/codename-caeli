# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
inputfile = '../datasets/Final_Air_Quality_Data.csv'
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# %%
#States are clustered according to 2014 data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns# Visualize the plot
from sklearn.preprocessing import MinMaxScaler


# %%
df = pd.read_csv(inputfile, encoding = "ISO-8859-1")
df = df[df['Year'] == 2014]
df = df.drop(['Year'], axis = 1)


# %%
# df = df[df['Year'] == 2014]
# df = df.drop(['Year'], axis = 1)


# %%
def showdist(df):
    fig, ax = plt.subplots(1, 3, figsize=(20,5))
    sns.distplot(df['so2'], ax = ax[0])
    sns.distplot(df['no2'], ax = ax[1])
    sns.distplot(df['rspm'], ax = ax[2])
    # plt.show()
# showdist(df)


# %%
# from sklearn.preprocessing import power_transform# Extract the specific column and convert it as a numpy array
X = df[['so2', 'no2', 'rspm']].values# Transform the data
# X = df[['rspm']].values
# df2 = power_transform(X, method='yeo-johnson')


# %%
from sklearn.preprocessing import MinMaxScaler# Instantiate the object
scaler = MinMaxScaler()# Fit and transform the data
X = scaler.fit_transform(X)
X[:,0]


# %%
from sklearn.cluster import KMeans# To make sure our work becomes reproducible
np.random.seed(42) 
inertia = []# Iterating the process
for i in range(2, 10):
  # Instantiate the model
    model = KMeans(n_clusters=i)
  # Fit The Model
    model.fit(X)
  # Extract the error of the model
    inertia.append(model.inertia_)# Visualize the model
sns.pointplot(x=list(range(2, 10)), y=inertia)
plt.title('SSE on K-Means based on # of clusters')
# plt.show()


# %%
np.random.seed(42)# Instantiate the model
model = KMeans(n_clusters=5)# Fit the model
model.fit(X)# Predict the cluster from the data and save it
cluster = model.predict(X)# Add to the dataframe and show the result
df['cluster'] = cluster

with open('ClusterMembers.txt', 'w') as f:    
    for i in range(5):
        f.write("Cluster: " + str(i) + '\n')
        f.write("The Members: " + ' | '.join(list(df[df['cluster'] == i]['State'].values)) + '\n')
        f.write("Total Members: " + str(len(list(df[df['cluster'] == i]['State'].values))) + '\n')
        f.write('\n')

# %%
import seaborn as sns
import matplotlib.pyplot as plt# Create the dataframe to ease our visualization process
visualize = pd.DataFrame(model.cluster_centers_) #.reset_index()
visualize = visualize.T
visualize['column'] = ['so2', 'no2', 'rspm']
# visualize['column'] = ['rspm']
visualize = visualize.melt(id_vars=['column'], var_name='cluster')
visualize['cluster'] = visualize.cluster.astype('category')# Visualize the result
plt.figure(figsize=(12, 8))
sns.barplot(x='cluster', y='value', hue='column', data=visualize)

plt.xlabel("Cluster")
plt.ylabel('Pollutant\'s concentration')
plt.title('The cluster\'s characteristics')
plt.savefig('Cluster vs Pollutant\'s concentration.png')
# plt.show()

