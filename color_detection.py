import numpy as np
from sklearn.cluster import KMeans

def color_detect_kmeans(pixels):
    pixels = np.array(pixels, dtype=np.float32)

    # HSV
    normalized_pixels = pixels.copy()
    normalized_pixels[:, 0] /= 180
    normalized_pixels[:, 1] /= 255
    normalized_pixels[:, 2] /= 255

    # Phân cụm với K-means
    kmeans = KMeans(n_clusters=6, random_state=0, n_init=10)
    kmeans.fit(normalized_pixels)

    centroids = kmeans.cluster_centers_
    centroids[:, 0] *= 180
    centroids[:, 1] *= 255
    centroids[:, 2] *= 255

    cluster_labels = {}
    for i, centroid in enumerate(centroids):
        h, s, v = centroid
        if (h < 10 or h > 170) and s >= 100 and v >= 50:
            cluster_labels[i] = 'red'
        elif 10 <= h <= 24 and s >= 100 and v >= 50:
            cluster_labels[i] = 'orange'
        elif 25 <= h <= 39 and s >= 100 and v >= 50:
            cluster_labels[i] = 'yellow'
        elif 40 <= h <= 84 and s >= 100 and v >= 50:
            cluster_labels[i] = 'green'
        elif 85 <= h <= 129 and s >= 70 and v >= 50:
            cluster_labels[i] = 'blue'
        else:
            cluster_labels[i] = 'white'

    # Debug:
    # print("Input pixels (HSV):", pixels)
    # print("Centroids (HSV):", centroids)
    # print("Cluster labels:", cluster_labels)

    labels = kmeans.labels_
    color_names = [cluster_labels[label] for label in labels]

    return color_names