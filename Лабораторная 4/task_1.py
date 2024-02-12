if __name__ == "__main__":
    # Write your solution here
    class Shape:
        """Базовый класс Фигура"""

        def __init__(self, color: str) -> None:
            """
            Конструктор класса Фигура.

            Args:
                color: Цвет фигуры.

            """
            self.color = color

        def __str__(self) -> str:
            """
            Возвращает строковое представление фигуры.

            Returns:
                Строковое представление фигуры.

            """
            return f"This is a {self.color} shape"

        def __repr__(self) -> str:
            """
            Возвращает официальное строковое представление об объекте фигура.

            Returns:
                Официальное строковое представление об объекте фигура.

            """
            return f"Shape({self.color})"


    class Rectangle(Shape):
        """Дочерний класс Прямоугольник."""

        def __init__(self, color: str, width: float, height: float) -> None:
            """
            Конструктор класса Прямоугольник.

            Args:
                color: Цвет прямоугольника.
                width: Ширина прямоугольника.
                height: Высота прямоугольника.

            """
            super().__init__(color)
            self.width = width
            self.height = height

        def __str__(self) -> str:
            """
            Перегруженный метод, добавляет информацию о параметрах фигуры в строковое представление.
            Возвращает строковое представление прямоугольника.

            Returns:
                Строковое представление прямоугольника.

            """
            return f"This is a {self.color} rectangle with width {self.width} and height {self.height}"

        def area(self) -> float:
            """
            Унаследованный метод.
            Возвращает площадь прямоугольника.

            Returns:
                Площадь прямоугольника.

            """
            return self.width * self.height

        def perimeter(self) -> float:
            """
            Унаследованный метод.
            Возвращает периметр прямоугольника.

            Returns:
                Периметр прямоугольника.

            """
            return 2 * (self.width + self.height)


    class Circle(Shape):
        """Дочерний класс Круг."""

        def __init__(self, color: str, radius: float) -> None:
            """
            Конструктор класса Круг.

            Args:
                color: Цвет круга.
                radius: Радиус круга.

            """
            super().__init__(color)
            self.radius = radius

        def __str__(self) -> str:
            """
            Перегруженный метод, добавляет информацию о параметрах фигуры в строковое представление.
            Возвращает строковое представление круга.

            Returns:
                Строковое представление круга.

            """
            return f"This is a {self.color} circle with radius {self.radius}"

        def area(self) -> float:
            """
            Унаследованный метод.
            Возвращает площадь круга.

            Returns:
                Площадь круга.

            """
            return 3.14 * self.radius ** 2

        def perimeter(self) -> float:
            """
            Унаследованный метод.
            Возвращает периметр круга.

            Returns:
                Периметр круга.

            """
            return 2 * 3.14 * self.radius


    circle = Circle("red", 3)
    print(circle)  # This is a red circle with radius 3
    print(circle.area())  # 28.27433..

    rectangle = Rectangle("green", 5, 7)
    print(rectangle)  # This is a green rectangle with width 5 and height 7
    print(rectangle.perimeter())  # 24.0
    pass
