class Vacancy:
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def __str__(self):
        return (f"Вакансия: {self.title}, Зарплата: {self.salary}, Ссылка: {self.url}, "
                f"Описание: {self.description[:30]}...")

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

    @classmethod
    def create_objects_from_dicts(cls, vacancies_info):
        vacancies = []
        for v in vacancies_info:
            salary = v.get('salary')
            salary_from = (salary.get('from', 0) if salary and isinstance(salary, dict) else 0)

            vacancy = cls(
                title=v['name'],
                url=v['alternate_url'],
                salary=cls.validate_salary(salary_from),
                description=v.get('snippet', {}).get('requirement', '') or ''
            )
            vacancies.append(vacancy)
        return vacancies
