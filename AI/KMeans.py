from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist, squareform
import os

# Define the relative path to data.csv from the AI folder
script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of KMeans.py
data_path = os.path.join(script_dir, '..', 'data.csv')  # Move up one level to parent folder

# scaling the data
X = pd.read_csv("test.csv")
names = X['NAME']
X = X.drop('NAME',axis=1)

# fitting the model
scaledX = StandardScaler().fit_transform(X)
normedX = pd.DataFrame(normalize(scaledX))

# fitting the model
kmeans = KMeans(n_clusters=20, random_state=0, n_init="auto").fit(normedX)
clusters = kmeans.cluster_centers_
kmeans_labels = kmeans.predict(normedX)

# pca for visualization of data, graphing the data
pca = PCA(n_components=2)
projectedX = pca.fit_transform(normedX)
plt.scatter(projectedX[:,0],projectedX[:,1],c="blue")
plt.scatter(clusters[:,0],clusters[:,1],c="orange")

# creating dictionary for every individual
clusters_dict = {i: [] for i in range(20)}
for label, name in zip(kmeans_labels, names):
    clusters_dict[label].append(name)

# scoring and assigning
top_matches = {}
all_scores = []
for cluster_id, users in clusters_dict.items():
    if len(users) > 1:
        # creating the indices for each person
        indices = [names[names == member].index[0] for member in users]
        cluster_data = normedX.iloc[indices].to_numpy()
        # getting the euclidean distances between all people
        distances = squareform(pdist(cluster_data, metric='euclidean'))
        
        for i, person_index in enumerate(indices):
            person_name = names[person_index]
            closest_indices = distances[i].argsort()[1:6]
            scores = [1 / (1 + distances[i][j]) for j in closest_indices]
            all_scores.extend(scores)
            top_matches[person_name] = [(users[j], score) for j, score in zip(closest_indices, scores)]

# Printing matches with scores and similar attributes: making it look nicer
for person in sorted(top_matches.keys(), key=lambda x: int(x.split('_')[1])):
    match = top_matches[person][0]
    # score normalization
    norm_score = (0.5+(match[1]-min(all_scores))**.7/(max(all_scores)-min(all_scores))**.7*.5)
    match_info = f"{match[0]} (Score: {norm_score:.4f})"
    print(f"Top matches for {person}: {match_info}")


plt.show()
