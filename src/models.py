class Vacancy:
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description
        }

    @staticmethod
    def validate_salary(salary):
        if salary is None or (isinstance(salary, str) and salary.strip() == "Зарплата не указана"):
            return 0  # Возвращаем 0 вместо строки
        elif isinstance(salary, (int, float)):
            return salary
        return 0  # Если salary не указана или неверна, тоже возвращаем 0
