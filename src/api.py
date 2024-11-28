import requests
from abc import ABC, abstractmethod


class Vacancy:
    """Класс для представления вакансии"""

    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def __str__(self):
        return f"{self.title}: {self.salary}, {self.url}"


class AbstractHeadHunterAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        """Получение вакансий по ключевому слову."""
        pass


class HeadHunterAPI(AbstractHeadHunterAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        """Инициализация сессии для работы с API HeadHunter."""
        self._session = requests.Session()

    def get_vacancies(self, keyword):
        """Получает вакансии по ключевому слову."""
        params = {
            "text": keyword,
            "area": 113,  # Москва
            "per_page": 100
        }

        try:
            response = self._session.get(self.BASE_URL, params=params)
            response.raise_for_status()  # Проверка на ошибки HTTP
            vacancies_data = response.json().get('items', [])
            # Создаем экземпляры класса Vacancy с проверкой зарплаты
            return [Vacancy(
                title=v['name'],
                url=v['alternate_url'],
                salary=v.get('salary', {}).get('from', 'Зарплата не указана'),
                description=v.get('snippet', {}).get('requirement', '')
            ) for v in vacancies_data]
        except requests.RequestException as e:
            print(f"Ошибка при подключении к API: {e}")
            return []
