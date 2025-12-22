import math

class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def add(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def add2(self, other: 'Vector2D') -> None:
        self.x += other.x
        self.y += other.y

    def sub(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def sub2(self, other: 'Vector2D') -> None:
        self.x -= other.x
        self.y -= other.y

    def mult(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    def mult2(self, scalar: float) -> None:
        self.x *= scalar
        self.y *= scalar

    def __str__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def scalar_product(self, other: 'Vector2D') -> float:
        return self.x * other.x + self.y * other.y

    def cos(self, other: 'Vector2D') -> float:
        dot = self.scalar_product(other)
        len_self = self.length()
        len_other = other.length()
        if len_self == 0 or len_other == 0:
            return 0.0
        return dot / (len_self * len_other)

    def equals(self, other: 'Vector2D') -> bool:
        return self.x == other.x and self.y == other.y



