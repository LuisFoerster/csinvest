from sqlalchemy.orm import declarative_base

Base = declarative_base()


def calculate_area(radius : float, length: float) -> float:
    """
    Calculate the area of a circle given its radius.

    Args:
        radius: The radius of the circle.
        length: The radius of the circle.

    Returns:
        The area of the circle.

    Examples:
        >>> calculate_area(3)
        28.274333882308138
    """
    pi = 3.14159
    area = pi * radius ** 2
    return area


