"""Write navigation function."""


class BadMoveError(Exception):
    """Bad move."""


def move(position: tuple[int, int], direction: str) -> tuple[int, int]:
    """Update position with move."""
    if direction not in ["north", "south", "east", "west"]:
        raise BadMoveError("Bad move!")

    x = position[0]
    y = position[1]
    if direction == "north":
        y += 1
    elif direction == "south":
        y -= 1
    elif direction == "east":
        x += 1
    else:
        x -= 1

    return (x, y)
