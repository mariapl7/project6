import requests
import json
from abc import ABC, abstractmethod
from src.models import Vacancy


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

    @staticmethod
    def save_vacancies_to_file(vacancies_list, filename='vacancies.json'):
        """Сохранение списка вакансий в файл JSON."""
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump([vacancy.to_dict() for vacancy in vacancies_list], f, ensure_ascii=False, indent=4)

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

            vacancies_list = []  # Переименование переменной для избежания конфликта имен
            for v in vacancies_data:
                salary = v.get('salary')
                salary_from = (salary.get('from', 0)
                               if salary and isinstance(salary, dict) else 0)

                vacancy = Vacancy(
                    title=v['name'],
                    url=v['alternate_url'],
                    salary=Vacancy.validate_salary(salary_from),  # Обращение через класс
                    description=v.get('snippet', {}).get('requirement', '') or ''
                )
                vacancies_list.append(vacancy)

            # Сохранение вакансий в файл
            self.save_vacancies_to_file(vacancies_list)
            return vacancies_list  # Возврат списка вакансий
        except requests.RequestException as e:
            print(f"Ошибка при подключении к API: {e}")
            return []


if __name__ == "__main__":
    api = HeadHunterAPI()
    vacancies = api.get_vacancies("Разработчик Python")
    print(f"Найдено {len(vacancies)} вакансий.")
