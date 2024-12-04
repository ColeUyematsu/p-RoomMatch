from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, normalize
from scipy.spatial.distance import pdist, squareform
import os

# Define the relative path to data.csv from the AI folder
script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of Agglomerative.py
data_path = os.path.join(script_dir, '..', 'data.csv')  # Move up one level to parent folder

# Load the dataset
X = pd.read_csv(data_path)  # Load the dataset
names = X['id']  # Store the names to be used to label matches later
X = X.drop(columns=['id', 'user_id'], axis=1)  # Remove names column from the dataset (not used to train model)

# Determine the number of clusters as participants divided by 2
num_participants = len(X)  # Number of participants (rows in data.csv)
num_clusters = max(2, num_participants // 2)  # Ensure at least 2 clusters

# scaling the data
scaledX = StandardScaler().fit_transform(X)
normedX = pd.DataFrame(normalize(scaledX), columns=X.columns)

# fitting the model
kmeans = KMeans(n_clusters=num_participants, random_state=0, n_init="auto").fit(normedX)
clusters = kmeans.cluster_centers_
kmeans_labels = kmeans.predict(normedX)

# pca for visualization of data, graphing the data
pca = PCA(n_components=2)
projectedX = pca.fit_transform(normedX)
plt.scatter(projectedX[:, 0], projectedX[:, 1], c="blue")
plt.scatter(clusters[:, 0], clusters[:, 1], c="orange")

# creating dictionary for every individual
clusters_dict = {i: [] for i in range(num_participants)}
for label, name in zip(kmeans_labels, names):
    clusters_dict[label].append(name)

# scoring and assigning
top_matches = {}
for cluster_id, users in clusters_dict.items():
    if len(users) > 1:
        # creating the indices for each person
        indices = [names[names == member].index[0] for member in users]
        cluster_data = normedX.iloc[indices].to_numpy()
        # getting the euclidean distances between all people
        distances = squareform(pdist(cluster_data, metric='euclidean'))

        # loop to go through very person; scoring the distances for everyone
        for i, person_index in enumerate(indices):
            person_name = names[person_index]
            closest_indices = distances[i].argsort()[1:6]
            matches = []
            for j in closest_indices:
                match_index = indices[j]
                match_name = names[match_index]
                score = 1 / (1 + distances[i][j])

                # getting the most similar attributes
                person_data = normedX.iloc[person_index]
                match_data = normedX.iloc[match_index]
                differences = abs(person_data - match_data)
                similar_attributes = differences.nsmallest(3).index.tolist()

                matches.append((match_name, score, similar_attributes))
            top_matches[person_name] = matches

# Printing matches with scores and similar attributes: making it look nicer
for person in sorted(top_matches.keys(), key=lambda x: int(x.split('_')[1])):
    matches = top_matches[person]
    match_info = ', '.join([
        f"{match[0]} (Score: {match[1]:.2f}, Similar Attributes: {match[2]})"
        for match in matches
    ])
    print(f"Top matches for {person}: {match_info}")

plt.show()
