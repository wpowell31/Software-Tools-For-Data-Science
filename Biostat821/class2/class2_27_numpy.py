import numpy as np


def main():
    """Do things."""
    two_d = np.array([[1, 2, 3], [4, 5, 6]])
    print(two_d)
    print(two_d.shape)

    one_d = np.array([7, 8, 9])
    print(one_d)
    print(one_d.shape)

    zero_d = np.array(10)
    print(zero_d)
    print(zero_d.shape)

    print(two_d @ two_d.T)


if __name__ == "__main__":
    main()
