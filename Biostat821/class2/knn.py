"""Implement KNN.
    Authors: Will Powell and Nick Bachelder."""
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1, 1], [1, 0], [3, 3], [3, 2], [5, 4]])
y = np.array([1, 1, 2, 2, 2])


def distance(x1, x2):
    """Calculates distance between two points"""
    return np.linalg.norm(x1 - x2)


class KNNClassifier:
    def __init__(self, k, X, y):
        self.k = k
        self.X = X
        self.y = y

    def predict(self, x_test):
        distances = []
        for i in range(X.shape[0]):
            x_train = X[i, :]
            y_train = y[i]
            val_distance = distance(x_train, x_test)
            distances.append([val_distance, y_train])

        distances = np.array(distances)
        distances = distances[np.argsort(distances[:, 0])]
        values, counts = np.unique(distances[0:self.k, 1], return_counts=True)
        max_count_index = np.argmax(counts)
        y_pred = values[max_count_index]
        return y_pred


knn = KNNClassifier(3, X, y)


def plot_knn():
    """visualize the knn."""
    # Define the range of the plot
    x_min, x_max = int(X[:, 0].min() - 1), int(X[:, 0].max() + 1)
    y_min, y_max = int(X[:, 1].min() - 1), int(X[:, 1].max() + 1)
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100)
    )

    Z = np.zeros((100, 100))
    for i in range(100):
        for j in range(100):
            Z[i, j] = knn.predict(np.array([xx[0, i], yy[j, 0]]))

    # Plot the decision area
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[:, 0], X[:, 1], c=y, alpha=0.8)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("KNN decision area")
    plt.show()


plot_knn()
