import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, normalize
from scipy.spatial.distance import pdist, squareform
import scipy.cluster.hierarchy as shc
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

print(f"Number of participants: {num_participants}")
print(f"Number of clusters: {num_clusters}")

# Scale and normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_normalized = normalize(X_scaled)
X_normalized = pd.DataFrame(X_normalized)

# Reduce dimensions using principal component analysis for dendrogram plotting
pca = PCA(n_components=2)
X_principal = pca.fit_transform(X_normalized)
X_principal = pd.DataFrame(X_principal, columns=['P1', 'P2'])

# Create a dendrogram to visualize clusters
plt.figure(figsize=(12, 8))
plt.title(f'Dendrogram for Roommate Preferences ({num_clusters} Clusters)')
dendrogram = shc.dendrogram(shc.linkage(X_principal, method='ward'))

# Perform Agglomerative Clustering
ac = AgglomerativeClustering(n_clusters=num_clusters)  # Set dynamic number of clusters
labels = ac.fit_predict(X_normalized)  # Fit clustering model

# Assert valid clustering
assert len(labels) == len(names), "Some individuals were not assigned to a cluster."
assert len(set(labels)) == num_clusters, f"The clustering did not result in {num_clusters} clusters."

# Organize individuals into clusters
clusters = {i: [] for i in range(num_clusters)}
for label, name in zip(labels, names):
    clusters[label].append(name)  # Group names by cluster labels

# Calculate similarity score within each cluster
output_data = {}
for cluster_id, members in clusters.items():
    if len(members) > 1:  # Process only clusters with multiple members
        indices = [names[names == member].index[0] for member in members]
        cluster_data = X_normalized.iloc[indices].to_numpy()
        distances = squareform(pdist(cluster_data, metric='euclidean'))
        max_distance = distances.max()
        similarity_scores = 1 - (distances / max_distance)

        for i, person_index in enumerate(indices):
            person_name = names[person_index]  # Get the person's name
            closest_index = distances[i].argsort()[1]  # Find the closest match
            closest_score = similarity_scores[i, closest_index]

            # Adjust the score to a 0.5-1 scale
            adjusted_score = 0.5 + closest_score * 0.5

            # Format the match with the adjusted score
            match_name = members[closest_index]
            output_data[person_name] = f"{match_name} (score: {round(adjusted_score, 2)})"

# Save clustering results to a CSV file
output_df = pd.DataFrame(list(output_data.items()), columns=['Person', 'Top Match'])
output_csv_path = os.path.join(script_dir, '..', 'Agglomerative_top_matches.csv')
output_df.to_csv(output_csv_path, index=False)

print(f"Top matches saved to '{output_csv_path}'.")

# Visualize clustering results
plt.figure(figsize=(8, 8))
plt.scatter(X_principal['P1'], X_principal['P2'], c=labels, cmap='tab20', s=50)
plt.title(f"Agglomerative Clustering ({num_clusters} Clusters)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.colorbar(label="Cluster Label")
plt.show()