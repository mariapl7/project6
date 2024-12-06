import unittest
import requests
from unittest.mock import patch
from src.utils import load_json_file, save_json_file, is_duplicate


class HeadHunterAPI:
    @staticmethod
    def get_vacancies(search_query):
        """Получает список вакансий по заданному запросу."""
        url = f'https://api.hh.ru/vacancies?text={search_query}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['items']
        else:
            return []


def user_interface():
    """Главный интерфейс пользователя для взаимодействия с API HeadHunter."""
    filename = "data.json"
    hh_api = HeadHunterAPI()

    while True:
        print("1. Показать вакансии")
        print("2. Добавить вакансию")
        print("3. Удалить вакансию")
        print("4. Выход")
        choice = input("Введите номер действия: ")

        if choice == '1':
            vacancies = hh_api.get_vacancies("Python")
            for v in vacancies:
                print(f"- {v['name']}: {v['salary']} р. (Ссылка: {v['alternate_url']})")
            continue  # Для тестов упростим выход

        elif choice == '2':
            title = "Тестовая вакансия"
            salary = "100000"
            new_vacancy = {"title": title, "salary": salary}

            existing_data = load_json_file(filename)
            if not is_duplicate(existing_data, title):
                existing_data.append(new_vacancy)
                save_json_file(filename, existing_data)

        elif choice == '3':
            title = "Тестовая вакансия"
            existing_data = load_json_file(filename)
            existing_data = [item for item in existing_data if item['title'] != title]
            save_json_file(filename, existing_data)

        elif choice == '4':
            break


class TestHeadHunterAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_vacancies_success(self, mock_get):
        """Тестирование успешного получения вакансий из API."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'items': [{'name': 'Python Developer', 'salary': 120000, 'alternate_url': 'http://example.com'}]
        }

        api = HeadHunterAPI()
        vacancies = api.get_vacancies("Python")

        # Проверка результата
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['name'], 'Python Developer')
        self.assertEqual(vacancies[0]['salary'], 120000)

    @patch('requests.get')
    def test_get_vacancies_failure(self, mock_get):
        """Тестирование обработки ошибки при получении вакансий из API."""
        mock_get.return_value.status_code = 404

        api = HeadHunterAPI()
        vacancies = api.get_vacancies("Python")

        # Проверка, что вернулся пустой список
        self.assertEqual(vacancies, [])


class TestUserInterface(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '4'])  # Имитация ввода для показа вакансий, затем выхода
    @patch('requests.get')
    def test_user_interface_show_vacancies(self, mock_get, mock_input):
        """Тестирование интерфейса пользователя при показе вакансий."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'items': [{'name': 'Python Developer', 'salary': 120000, 'alternate_url': 'http://example.com'}]
        }

        with patch('builtins.print') as mock_print:
            user_interface()  # Запускаем интерфейс

            # Проверки, ожидаем, что печатаются правильные данные
            mock_print.assert_any_call("1. Показать вакансии")
            mock_print.assert_any_call("- Python Developer: 120000 р. (Ссылка: http://example.com)")


if __name__ == "__main__":
    unittest.main()
