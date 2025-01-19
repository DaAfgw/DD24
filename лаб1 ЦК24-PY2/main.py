import doctest

class Book: #Класс, описывающий книгу

    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("Преступление и наказание", "Ф. М. Достоевский", 672)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть веден строкой")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

        self.current_page = 0  # Текущая страница, на которой находится читатель

    def is_finished(self) -> bool:
        """
        Проверить, прочитана ли книга

        :return: True, если книга прочитана, иначе False

        Примеры:
        >>> book = Book("Преступление и наказание", "Ф. М. Достоевский", 672)
        >>> book.is_finished()
        False
        """
        return self.current_page >= self.pages


    def bookmark(self, page: int) -> None:
        """
        Добавить закладку на указанную страницу

        :param page: Номер страницы для закладки

        Примеры:
        >>> book = Book("Преступление и наказание", "Ф. М. Достоевский", 672)
        >>> book.bookmark(100)
        """
        if not isinstance(page, int):
            raise TypeError("Номер страницы должен быть целым числом")
        if page < 1 or page > self.pages:
            raise ValueError("Номер страницы должен быть в пределах книги")

        self.current_page = page



class Fridge: #Класс, описывающий холодильник

    def __init__(self, brand: str, capacity: int, temperature: float):
        """
        Создание и подготовка к работе объекта "Холодильник"

        :param brand: Марка холодильника
        :param capacity: Общий объем холодильника (в литрах)
        :param temperature: Текущая температура внутри холодильника

        Примеры:
        >>> fridge = Fridge("Samsung", 300, 4.0)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка холодильника должна быть строкой")
        self.brand = brand

        if not isinstance(capacity, int):
            raise TypeError("Объем холодильника должен быть целым числом")
        if capacity <= 0:
            raise ValueError("Объем холодильника должен быть положительным числом")
        self.capacity = capacity

        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть числом")
        if temperature < -30 or temperature > 10:
            raise ValueError("Температура холодильника должна быть в диапазоне от -30 до 10 градусов")
        self.temperature = temperature

        ...

    def open_door(self) -> None:
        """
        Открыть дверцу холодильника

        Примеры:
        >>> fridge = Fridge("Samsung", 300, 4.0)
        >>> fridge.open_door()
        """
        ...

    def close_door(self) -> None:
        """
        Закрыть дверцу холодильника

        Примеры:
        >>> fridge = Fridge("Samsung", 300, 4.0)
        >>> fridge.close_door()
        """
        ...


class OnlineCourse: #Класс, описывающий онлайн-курс

    def __init__(self, title: str, instructor: str, total_lessons: int):
        """
        Создание и подготовка к работе объекта "Онлайн-курс"

        :param title: Название курса
        :param instructor: Имя преподавателя
        :param total_lessons: Общее количество уроков в курсе

        Примеры:
        >>> course = OnlineCourse("Английский", "Иван Иванов", 10)
        """
        if not isinstance(title, str):
            raise TypeError("Название курса должно быть строкой")
        self.title = title

        if not isinstance(instructor, str):
            raise TypeError("Имя преподавателя должно быть строкой")
        self.instructor = instructor

        if not isinstance(total_lessons, int):
            raise TypeError("Общее количество уроков должно быть целым числом")
        if total_lessons <= 0:
            raise ValueError("Общее количество уроков должно быть положительным числом")
        self.total_lessons = total_lessons


    def progress(self) -> float:
        """
        Рассчитать прогресс в процентах

        :return: Прогресс в процентах (от 0 до 100)

        Примеры:
        >>> course = OnlineCourse("Английский", "Иван Иванов", 10)
        >>> course.progress()
        """
        ...

    def reset_progress(self) -> None:
        """
        Сбросить прогресс прохождения курса

        Примеры:
        >>> course = OnlineCourse("Английский", "Иван Иванов", 10)
        >>> course.reset_progress()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации