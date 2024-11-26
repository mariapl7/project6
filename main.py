import requests
from src.utils import load_json_file, save_json_file, is_duplicate


class Vacancy:
    """Класс для представления вакансии"""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name}: {self.salary if self.salary else 'Не указана'}"


class HeadHunterAPI:
    """Класс для взаимодействия с API HeadHunter"""

    @staticmethod
    def get_vacancies(search_query):
        """Получает список вакансий по заданному запросу"""
        url = f'https://api.hh.ru/vacancies?text={search_query}'
        response = requests.get(url)
        if response.status_code == 200:
            vacancies_data = response.json()['items']
            # Создаем экземпляры класса Vacancy
            return [Vacancy(v['name'], v.get('salary')) for v in vacancies_data]
        else:
            print(f"Ошибка при получении вакансий: {response.status_code}")
            return []


def user_interface():
    """Интерфейс взаимодействия с пользователем"""
    filename = "data.json"

    while True:
        print("\nВыберите действие:")
        print("1. Показать вакансии")
        print("2. Добавить вакансию")
        print("3. Удалить вакансию")
        print("4. Выход")
        choice = input("Введите номер действия: ")

        if choice == '1':
            hh_api = HeadHunterAPI()
            vacancies = hh_api.get_vacancies("Python")
            print("Список вакансий:")
            for vacancy in vacancies:
                print(f"- {vacancy}")

        elif choice == '2':
            title = input("Введите заголовок вакансии: ")
            salary = input("Введите зарплату: ")
            new_vacancy = Vacancy(title, salary)

            existing_data = load_json_file(filename)
            if not is_duplicate(existing_data, title):
                existing_data.append({"title": new_vacancy.name, "salary": new_vacancy.salary})
                save_json_file(filename, existing_data)
                print("Вакансия добавлена.")
            else:
                print("Вакансия с таким заголовком уже существует")

        elif choice == '3':
            title = input("Введите заголовок вакансии для удаления: ")
            existing_data = load_json_file(filename)
            updated_data = [item for item in existing_data if item['title'] != title]
            save_json_file(filename, updated_data)
            print("Вакансия удалена, если она существовала")

        elif choice == '4':
            print("Выход...")
            break

        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    user_interface()
