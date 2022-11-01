class Pizza:
    """Basic Pizza"""
    def __init__(self, ingredients: list[str], size: str):
        self._ingredients = ingredients
        self.size = size

    def dict(self) -> dict:
        """returns dict like {pizza_title: ingredients}"""
        return {self.__class__.__name__: self._ingredients}

    @property
    def size(self) -> str:
        """returns pizza size"""
        return self._size

    @size.setter
    def size(self, value: str) -> None:
        """Pizza size setter. Possible values: 'L', 'XL'"""
        if value not in ['L', 'XL']:
            raise ValueError(f'Size of pizza must be L or XL, not {value}.')
        self._size = value

    def __eq__(self, other) -> bool:
        return self.dict() == other.dict() and self.size == other.size


class Margherita(Pizza):
    """Margherita"""
    def __init__(self, size: str = 'L'):
        ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
        super().__init__(ingredients, size)


class Pepperoni(Pizza):
    """Pepperoni"""
    def __init__(self, size: str = 'L'):
        ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
        super().__init__(ingredients, size)


class Hawaiian(Pizza):
    """Hawaiian"""
    def __init__(self, size: str = 'L'):
        ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        super().__init__(ingredients, size)
