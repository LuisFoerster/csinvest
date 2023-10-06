# Conventions



Ordner und Files werden nach Snakecase-convention benannt

Variablen sowie Funktionen und Methoden werden nach Snakecase-convention benannt:

```python
def one_function():
    pass

one_int = 0
```

Klassen werden nach Camelcase-convention benannt

```python
class OneClass:
 pass
```

Funktionen und Classen haben einen Docsstring nach PEP 257:

```python
def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.

    Examples:
        >>> calculate_area(3)
        28.274333882308138
    """
    pi = 3.14159
    area = pi * radius ** 2
    return area

class Car:
    """
    Represents a car object.

    Attributes:
        make (str): The make of the car (e.g., "Toyota", "Ford").
        model (str): The model of the car (e.g., "Camry", "Mustang").
        year (int): The manufacturing year of the car.
        color (str): The color of the car.
    """

    def __init__(self, make, model, year, color):
        """
        Initializes a new Car instance.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
            year (int): The manufacturing year of the car.
            color (str): The color of the car.
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color


```