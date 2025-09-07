from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('user_dataset.csv')
scaler=StandardScaler()

scaled=scaler.fit_transform(df[['frequency','monetary_value','unique_products','review_count_individual','average_rating_individual','average_discount_individual_product']])
scaled_df=pd.DataFrame(scaled,index=df.index, columns=['frequency','monetary_value','unique_products','review_count_individual','average_rating_individual','average_discount_individual_product'])    

Max_k=15


inetria=[]
k_range=range(2,Max_k+1)

for k in k_range:
    kmeans=KMeans(n_clusters=k, random_state=42, max_iter=10000)
    kmeans.fit_predict(scaled_df[["frequency",'monetary_value','average_rating_individual']])
    inetria.append(kmeans.inertia_)

plt.figure(figsize=(14,6))
plt.plot(k_range, inetria, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.xticks(k_range)
plt.grid(True)
plt.savefig('elbow_method.png')
plt.show()


# Elbow method suggests optimal k at 4 for this case


optimal_k=4

kmeans=KMeans(n_clusters=optimal_k, random_state=42, max_iter=10000)
df['cluster']=kmeans.fit_predict(scaled_df[["frequency",'monetary_value','average_rating_individual']])


cluster_colors={0:'red', 1:'blue', 2:'green', 3:'purple', 4:'orange'}

colours=df['cluster'].map(cluster_colors)

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111, projection='3d')
ax.scatter(scaled_df['frequency'], scaled_df['monetary_value'], scaled_df['average_rating_individual'], c=colours, s=50)
ax.set_xlabel('Frequency')
ax.set_ylabel('Monetary Value')
ax.set_zlabel('Average Rating Individual')
ax.set_title('3D Scatter Plot of Clusters')
plt.savefig('3d_clusters.png')
plt.show()
