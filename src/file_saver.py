import json


class JSONFileHandler:
    """Обрабатывает сохранение, загрузку и удаление данных вакансий в формате JSON."""

    def __init__(self, filename='vacancies.json'):
        """Инициализирует обработчик файла JSON."""
        self.filename = filename

    def save_data(self, vacancies):
        """Сохранение списка вакансий в файл JSON."""
        with open(self.filename, 'w', encoding="utf-8") as f:
            json.dump([vacancy.to_dict() for vacancy in vacancies], f, ensure_ascii=False, indent=4)

    def delete_data(self, title):
        """Удаление вакансии из файла JSON по заголовку."""
        try:
            with open(self.filename, 'r', encoding="utf-8") as f:
                data = json.load(f)

            updated_data = [vac for vac in data if vac['title'] != title]

            with open(self.filename, 'w', encoding="utf-8") as f:
                json.dump(updated_data, f, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print("Файл не найден.")
        except json.JSONDecodeError:
            print("Ошибка в формате JSON.")

    def load_data(self):
        """Загрузка вакансий из файла JSON."""
        try:
            with open(self.filename, 'r', encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Файл не найден.")
            return []
        except json.JSONDecodeError:
            print("Ошибка в формате JSON.")
            return []
