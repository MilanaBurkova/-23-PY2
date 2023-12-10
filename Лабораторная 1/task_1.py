# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Matrix:
    def __init__(self, rows: int, cols: int):
        """
        Создание и подготовка к работе объекта "Матрица"

        :param rows: Количество строк матрицы
        :param cols: Количество столбцов матрицы

        Примеры:
        >>> matrix = Matrix(4, 3)  # инициализация экземпляра класса
        """
        if not isinstance(rows, int):
            raise TypeError("Количество строк матрицы должно быть типа int")
        if rows <= 0:
            raise ValueError("Количество строк матрицы должно быть положительным числом")
        self.rows = rows

        if not isinstance(cols, int):
            raise TypeError("Количество столбцов матрицы должно быть типа int")
        if cols <= 0:
            raise ValueError("Количество столбцов матрицы должно быть положительным числом")
        self.cols = cols

    def matrix_null(self) -> list:
        """
        Функция которая создает нулевую матрицу

        :return: Нулевая матрица

        Примеры:
        >>> matrix = Matrix(2, 3)
        >>> matrix.matrix_null()
        """
        ...

    def automatic_filling(self) -> list:
        """
        Автоматическое заполнение значений матрицы

        :return: Матрица со значениями

        Примеры:
        >>> matrix = Matrix(4, 5)
        >>> matrix.automatic_filling()
        """
        ...

    def identity(self) -> list:
        """
        Создание единичной матрицы
        :raise ValueError: Если количество строк матрицы не равно количеству столбцов матрицы то возвращается ошибка

        :return: Единичная матрица

        Примеры:
        >>> matrix = Matrix(2, 2)
        >>> matrix.identity()
        """
        ...


class Engine:
    def __init__(self, power: int, synchronous_speed: int):
        """
        Создание и подготовка к работе объекта "Двигатель"

        :param power: Мощность двигателя, Вт
        :param synchronous_speed: Синхронная частота вращения, об/мин

        Примеры:
        >>> engine = Engine(8000, 750)  # инициализация экземпляра класса
        """
        if not isinstance(power, int):
            raise TypeError("Мощность двигателя должна быть типа int")
        if power <= 0:
            raise ValueError("Мощность двигателя должна быть положительным числом")
        self.power = power

        if not isinstance(synchronous_speed, int):
            raise TypeError("Синхронная частота вращения должна быть типа int")
        if synchronous_speed <= 0:
            raise ValueError("Синхронная частота вращения должна быть положительным числом")
        self.synchronous_speed = synchronous_speed

    def angular_speed(self, engine_slip: float) -> float:
        """
        Функция, которая вычисляет номинальную угловую скорость двигателя
        :param engine_slip: Величина скольжения двигателя, %

        :return: Номинальная угловая скорость двигателя, рад/с

        Примеры:
        >>> engine = Engine(8000, 750)
        >>> engine.angular_speed(9.6)
        """
        if not isinstance(engine_slip, (int, float)):
            raise TypeError("Величина скольжения двигателя должна быть типа int или float")
        if engine_slip <= 0:
            raise ValueError("Величина скольжения двигателя должна быть положительным числом")
        ...

    def reduction_radius(self, linear_speed: float) -> float:
        """
        Функция, которая вычисляет радиус приведения (передаточное число)
        :param linear_speed: Линейная скорость выходного звена механизма, м/с

        :return: радиус приведения, м

        Примеры:
        >>> engine = Engine(8000, 750)
        >>> engine.reduction_radius(0.02)
        """
        if not isinstance(linear_speed, (int, float)):
            raise TypeError("Линейная скорость должна быть типа int или float")
        if linear_speed <= 0:
            raise ValueError("Линейная скорость должна быть положительным числом")
        ...

    def rated_torque(self, rated_angular_speed: float) -> float:
        """
        Номинальный момент на двигателе
        :param rated_angular_speed: Номинальная угловая скорость, рад/с

        :return: Номинальный момент на двигателе, Нм

        Примеры:
        >>> engine = Engine(8000, 750)
        >>> engine.rated_torque(70.5)
        """
        if not isinstance(rated_angular_speed, (int, float)):
            raise TypeError("Номинальная угловая скорость должна быть типа int или float")
        if rated_angular_speed <= 0:
            raise ValueError("Номинальная угловая скорость должна быть положительным числом")
        ...


class Robot:
    def __init__(self, type_of_robot: str, weight: float, width: float):
        """
        Создание и подготовка к работе объекта "Робот"

        :param type_of_robot: Тип робота
        :param weight: Масса робота, кг
        :param width: Ширина робота, см

        Примеры:
        >>> droid = Robot("R2D2", 2.5, 20)  # инициализация экземпляра класса
        """
        if not isinstance(type_of_robot, str):
            raise TypeError("Тип робота должен быть типа str")
        self.type_of_robot = type_of_robot

        if not isinstance(weight, (int, float)):
            raise TypeError("Масса должна быть типа int или float")
        if weight <= 0:
            raise ValueError("Масса должна быть положительным числом")
        self.weight = weight

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

    def speed(self, whell_diameter: float, angular_speed_of_rotation: float) -> float:
        """
        Функция, которая вычисляет скорость робота
        :param whell_diameter: Диаметр колес робота, см
        :param angular_speed_of_rotation: Угловая скорость вращения колес, рад/с
        :return: Скорость робота, м/с

        Примеры:
        >>> droid = Robot("R2D2", 2.5, 20)
        >>> droid.speed(10, 54.3)
        """
        if not isinstance(whell_diameter, (int, float)):
            raise TypeError("Диаметр колес робота должен быть типа int или float")
        if whell_diameter <= 0:
            raise ValueError("Диаметр колес робота должен быть положительным числом")

        if not isinstance(angular_speed_of_rotation, (int, float)):
            raise TypeError("Угловая скорость вращения колес должна быть типа int или float")
        if angular_speed_of_rotation <= 0:
            raise ValueError("Угловая скорость вращения колес должна быть положительным числом")
        ...

    def driving_time(self, path: float) -> float:
        """
        Функция, которая вычисляет время движения робота
        :param path: Путь, пройденный роботом, м

        :return: Время движения, с

        Примеры:
        >>> droid = Robot("R2D2", 2.5, 20)
        >>> droid.driving_time(100)
        """
        if not isinstance(path, (int, float)):
            raise TypeError("Путь должен быть типа int или float")
        if path <= 0:
            raise ValueError("Путь должен быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
