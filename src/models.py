class Vacancy:
    """Класс, представляющий вакансию."""
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
        if salary is None or salary == "Зарплата не указана":
            return "Зарплата не указана"
        try:
            return float(salary)
        except ValueError:
            raise ValueError("Некорректное значение зарплаты")

    @property
    def title(self):
        """Возвращает заголовок вакансии."""
        return self._title

    @property
    def url(self):
        """Возвращает ссылку на вакансию."""
        return self._url

    @property
    def salary(self):
        """Возвращает уровень зарплаты."""
        return self._salary

    @property
    def description(self):
        """Возвращает описание вакансии."""
        return self._description

    def __lt__(self, other):
        """Сравнивает зарплату с другой вакансией для определения меньшего."""
        return self._salary < other._salary

    def __gt__(self, other):
        """Сравнивает зарплату с другой вакансией для определения большего."""
        return self._salary > other._salary

    def __eq__(self, other):
        """Сравнивает зарплату с другой вакансией на равенство."""
        return self._salary == other._salary

    def __str__(self):
        """Возвращает строковое представление вакансии."""
        return f"{self._title}: {self.salary}, {self._url}"
