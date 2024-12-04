from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
import pandas as pd
import os


# GOAL: FIND THE 5 BEST MATCHES FOR A STUDENT (Person_2 for now) 
# USES GMM TO CREATE N CLUSTERS (using N = 5 clusters for now)
# FIND STUDENTS IN THE SAME CLUSTER as Person_2
# FIND 5 BEST MATCHES from the STUDENTS IN THE SAME CLUSTER AS Person_2 USING KNN

# Load the data that was previously stored
# Data is read into dataframe df - 34 Columns are the actual questions. Rows are responses of each person for each of the questions.
script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of Agglomerative.py
data_path = os.path.join(script_dir, '..', 'data.csv')  # Move up one level to parent folder

# Load the dataset
df = pd.read_csv(data_path)  # Load the dataset
names = df['id']  # Store the names to be used to label matches later
X = df.drop(columns=['id', 'user_id'], axis=1)  # Remove names column from the dataset (not used to train model)
clusters = len(X) // 2

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit GMM
gmm = GaussianMixture(n_components=clusters, random_state=42)  # n_components = 5. GMM will create 5 clusters.
gmm.fit(X_scaled)

# Predict cluster memberships
df['Cluster'] = gmm.predict(X_scaled)

# Choose a specific student (idx 0 is person_1, idx 1 is person 2)
student_idx = 1 # person_2
student_cluster = df.iloc[student_idx]['Cluster']

# Filter students in the same cluster as person_2
#same_cluster = df[df['Cluster'] == student_cluster]

# Exclude the specific student, person_2
#same_cluster = same_cluster[same_cluster['NAME'] != names.iloc[student_idx]]


# Combining GMM with KNN
# Use GMM to group students into clusters. Apply KNN within a cluster to find the closest matches

from sklearn.neighbors import NearestNeighbors

# Get cluster of a specific student
cluster_students = X_scaled[df['Cluster'] == student_cluster]
names_in_cluster = names[df['Cluster'] == student_cluster]

# Fit KNN on the cluster
# Will find the 6 nearest neighbors for Person_2 and then drop Person_2 from the list - get the 5 best matches
knn = NearestNeighbors(n_neighbors=1, metric='euclidean')
knn.fit(cluster_students)

# Find nearest neighbors within the cluster
distances, indices = knn.kneighbors([X_scaled[student_idx]])
matches = names_in_cluster.iloc[indices[0]]

matches = matches.drop(labels = matches[matches == 'Person_2'].index[0])

print(f"Top matches for {names.iloc[student_idx]}:")
print(matches)