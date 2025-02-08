class ConiferousTree:
    """
    Базовый класс для хвойных деревьев
    Определяет основные характеристики и методы, общие для всех хвойных деревьев
    """

    def __init__(self, name: str, height: float):
        """
        Конструктор класса ConiferousTree
        :param name: название дерева
        :param height: высота дерева в метрах
        """
        self._name = name  # непубличный атрибут, так как название не должно изменяться произвольно
        self._height = height  # непубличный атрибут для предотвращения произвольного изменения

    def needle_length_info(self) -> str:
        """
        Метод, который должен быть переопределён в дочерних классах
        Описывает длину хвои у разных деревьев
        """
        return "Длина хвои варьируется в зависимости от вида дерева"

    def __str__(self) -> str:
        return f"Хвойное дерево: {self._name}, высота: {self._height} м"

    def __repr__(self) -> str:
        return f"ConiferousTree(name={self._name!r}, height={self._height})"


class Pine(ConiferousTree):
    """
    Дочерний класс, представляющий сосну.
    """

    def __init__(self, name: str, height: float, needle_length: float):
        """
        Конструктор класса Pine.
        :param name: название дерева
        :param height: высота дерева в метрах
        :param needle_length: длина иголок в сантиметрах
        """
        super().__init__(name, height)
        self.needle_length = needle_length  # длина иголок доступна публично

    def needle_length_info(self) -> str:
        """
        Перегруженный метод. У сосен хвоя длинная
        """
        return f"У сосны длинные иголки, их средняя длина: {self.needle_length} см."

    def __str__(self) -> str:
        """
        Перегруженный метод, добавляющий информацию о длине иголок
        """
        return f"Сосна: {self._name}, высота: {self._height} м, длина иголок: {self.needle_length} см"

    def __repr__(self) -> str:
        return f"Pine(name={self._name!r}, height={self._height}, needle_length={self.needle_length!r})"


class Spruce(ConiferousTree):
    """
    Дочерний класс, представляющий ель.
    """

    def __init__(self, name: str, height: float, needle_length: float):
        """
        Конструктор класса Spruce
        :param name: название дерева
        :param height: высота дерева в метрах
        :param needle_length: длина иголок в сантиметрах
        """
        super().__init__(name, height)
        self.needle_length = needle_length  # длина иголок доступна публично

    def needle_length_info(self) -> str:
        """
        Перегруженный метод. У ели хвоя короткая
        """
        return f"У ели короткие иголки, их средняя длина: {self.needle_length} см."

    def __str__(self) -> str:
        """
        Перегруженный метод, добавляющий информацию о длине иголок
        """
        return f"Ель: {self._name}, высота: {self._height} м, длина иголок: {self.needle_length} см"

    def __repr__(self) -> str:
        return f"Spruce(name={self._name!r}, height={self._height}, needle_length={self.needle_length!r})"


if __name__ == "__main__":
    pine = Pine("Сосна", 20, 5)
    spruce = Spruce("Ель", 15, 2)

    print(pine)  # Сосна: Сосна обыкновенная, высота: 20 м, длина иголок: 5 см
    print(spruce)  # Ель: Ель европейская, высота: 15 м, длина иголок: 2 см

    print(pine.needle_length_info())  # У сосны длинные иголки, их средняя длина: 5 см.
    print(spruce.needle_length_info())  # У ели короткие иголки, их средняя длина: 2 см.
