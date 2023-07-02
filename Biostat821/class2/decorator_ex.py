"""Show decorator example."""
from typing import Callable, Any, Optional, TypeVar

T = TypeVar("T")


def decorate(fcn: Callable[[], Any]) -> Callable[[], Optional[T]]:
    """Decorate a function."""

    def maybe_do_thing() -> Optional[T]:
        """Maybe run fcn."""
        if 5 == 4:
            return fcn()
        else:
            print("Nope")
            return None

    return maybe_do_thing


@decorate
def plot_knn() -> None:
    """Plot something."""
    print("Here's my classifier")


# plot_knn = decorate(plot_knn)

plot_knn()
