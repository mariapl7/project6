import requests
from abc import ABC, abstractmethod


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
            return response.json().get('items', [])  # Возврат списка вакансий
        except requests.RequestException as e:
            print(f"Ошибка при подключении к API: {e}")
            return []
