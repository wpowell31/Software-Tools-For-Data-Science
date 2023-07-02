"""Run dunder example."""
from functools import cache


class Dinosaur:
    """Create the dinosaur class."""

    def __init__(self, name: str, height: float):
        """Initialize."""
        self.name = name
        self.height = height

    def __str__(self) -> str:
        """Create string method."""
        return f"{self.height}-foot-tall {self.name}"

    def __repr__(self) -> str:
        """Create repr method."""
        return f"Dinosaur({self.height}, {self.name})"

    def __eq__(self, other: object) -> bool:
        """Create equal magic method."""
        if not isinstance(other, Dinosaur):
            return False
        return self.name == other.name and self.height == other.height

    def __hash__(self) -> int:
        """Create hash magic method."""
        return hash(repr(self))


@cache
def shrink(dino: Dinosaur) -> Dinosaur:
    """Shrink the dinosaur."""
    dino.height -= 1
    return dino


if __name__ == "__main__":
    trex = Dinosaur("T-Rex", 30)
    triceratops = Dinosaur("Triceratops", 10)
    print(trex)
    # print([trex])
    # print(trex == "hello")
    # print(trex == trex)
    # print(trex == Dinosaur("T-Rex", 30))
    smaller_trex = shrink(trex)
    print(smaller_trex)
