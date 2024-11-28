class Vacancy:
    """Класс для представления вакансии."""
    __slots__ = [
        "_title",
        "_url",
        "_salary",
        "_description"
    ]

    def __init__(self, title, url, salary, description):
        """Инициализация экземпляра класса Vacancy."""
        self._title = title
        self._url = url
        self._salary = self._validate_salary(salary)
        self._description = description

    @staticmethod
    def _validate_salary(salary):
        """Проверяет корректность значения зарплаты."""
        if salary is None or salary.strip() == "Зарплата не указана":
            return "Зарплата не указана"
        try:
            # Удаляем все символы, кроме цифр и точки
            cleaned_salary = ''.join(filter(lambda x: x.isdigit() or x in '.-', str(salary)))
            return float(cleaned_salary) if cleaned_salary else "Зарплата не указана"
        except ValueError:
            raise ValueError("Некорректное значение зарплаты")

    def __str__(self):
        """Возвращает строковое представление вакансии."""
        return f"{self._title}: {self._salary}, {self._url}"
