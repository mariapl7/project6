import requests
from abc import ABC, abstractmethod


# Абстрактный класс для работы с API
class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        """Получение вакансий по ключевому слову."""
        pass


# Класс, работающий с API hh.ru
class HeadHunterAPI(AbstractAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        """Инициализация сессии для работы с API HeadHunter."""
        self._session = requests.Session()  # Создаем сессию для повторного использования настроек

    def _connect_to_api(self):
        """Приватный метод для отправки запроса к API. Проверяет статус ответа."""
        # Обычно здесь будет общая логика для проверки статуса, если потребуется
        pass

    def get_vacancies(self, keyword):
        """Получает вакансии по ключевому слову."""
        params = {
            "text": keyword,
            "area": 113,  # Москва
            "per_page": 100  # Количество вакансий на странице
        }

        response = self._session.get(self.BASE_URL, params=params)
        self._connect_to_api()  # Вызываем приватный метод подключения

        if response.status_code == 200:
            # Собираем данные ответа в формате списка словарей из ключа 'items'
            vacancy_list = response.json().get('items', [])
            return vacancy_list
        else:
            print(f"Error {response.status_code}: {response.text}")
            return []