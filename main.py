from src.api import HeadHunterAPI
from src.models import Vacancy
from src.file_saver import JSONFileHandler
import sys
import os

# Добавление папки src в PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))


def get_salary_input() -> int:
    """Запросить у пользователя желаемую зарплату."""
    while True:
        try:
            return int(input("Введите желаемую зарплату: "))
        except ValueError:
            print("Ошибка: Введите корректное числовое значение для зарплаты.")


def handle_deletion(json_handler: JSONFileHandler) -> None:
    """Обработать потенциальное удаление вакансий."""
    del_vacancy = input("Требуется что-нибудь удалить из файла? 'Да,Нет': ").strip().lower()
    if del_vacancy == 'да':
        titles_to_delete = input('Введите заголовки для удаления, разделенные запятыми: ')
        titles_list = [title.strip() for title in titles_to_delete.split(',')]
        for title in titles_list:
            confirm = input(f"Вы уверены, что хотите удалить вакансию '{title}'? (Да/Нет): ")
            if confirm.lower() == 'да':
                json_handler.delete_data(title)
                print(f"Вакансия '{title}' была удалена.")
            else:
                print(f"Вакансия '{title}' не была удалена.")


def user_interaction():
    api = HeadHunterAPI()
    json_handler = JSONFileHandler("vacancies.json")

    search_query = input("Введите поисковый запрос для вакансий: ")
    vacancies = api.get_vacancies(search_query)

    if not vacancies:
        print("Вакансии не найдены.")
        return

    while True:
        try:
            top_n = int(input("Введите количество топ вакансий по зарплате (N): "))
            if top_n <= 0:
                raise ValueError("Значение должно быть положительным.")
            break
        except ValueError as e:
            print(f"Ошибка: {e}. Пожалуйста, введите корректное значение.")

    top_vacancies = sorted(vacancies, key=lambda vac: vac.salary, reverse=True)[:top_n]
    print("\nТоп {} вакансий по зарплате:".format(top_n))
    for vacancy in top_vacancies:
        print(vacancy)

    keyword = input("Введите ключевое слово для фильтрации по описанию: ")
    filtered_vacancies = [vac for vac in vacancies if keyword.lower() in vac.description.lower()]

    if filtered_vacancies:
        print("\nВакансии с ключевым словом '{}':".format(keyword))
        for vacancy in filtered_vacancies:
            print(vacancy)
    else:
        print(f"\nВакансии с ключевым словом '{keyword}' не найдены.")

    handle_deletion(json_handler)


if __name__ == "__main__":
    user_interaction()
