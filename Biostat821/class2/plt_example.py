import matplotlib.pyplot as plt
import numpy as np


def main():
    X = np.random.multivariate_normal(
        mean=np.array([0, 0]), 
        cov=np.array([[1, 0], [0, 1]]),
        size=100,
    )
    # print(X)
    xs, ys = np.meshgrid(np.linspace(-3, 3, 10), np.linspace(-3, 3, 10))
    # print(xs, "\n", ys)
    plt.imshow(xs**2, extent=[-3,3,-3,3])
    plt.scatter(X[:, 0], X[:, 1])
    ax = plt.gca()
    ax.set_aspect("equal", adjustable="box")
    plt.show()


if __name__ == "__main__":
    main()
