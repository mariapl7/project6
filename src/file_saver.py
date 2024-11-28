import json
from abc import ABC, abstractmethod

class AbstractFileHandler(ABC):
    @abstractmethod
    def load_data(self):
        """Загружает данные из файла."""
        pass

    @abstractmethod
    def save_data(self, data):
        """Сохраняет данные в файл."""
        pass

    @abstractmethod
    def delete_data(self, title):
        """Удаляет данные из файла по заголовку."""
        pass

class JSONFileHandler(AbstractFileHandler):
    def __init__(self, filename="data.json"):
        """Инициализация обработчика JSON-файлов."""
        self._filename = filename

    def load_data(self):
        """Загружает данные из JSON-файла."""
        try:
            with open(self._filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if isinstance(data, list) else []  # Проверка на корректность
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Ошибка декодирования JSON. Файл может быть поврежден.")
            return []
        except Exception as e:
            print(f"Неизвестная ошибка при загрузке данных: {e}")
            return []

    def save_data(self, data):
        """Сохраняет данные в JSON-файл, проверяя на дубликаты."""
        if not isinstance(data, list):
            raise ValueError("Данные должны быть списком.")

        existing_data = self.load_data()
        titles = {item['title'] for item in existing_data}

        for item in data:
            if item['title'] not in titles:
                existing_data.append(item)
                titles.add(item['title'])

        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)

    def delete_data(self, title):
        """Удаляет данные из JSON-файла по заголовку."""
        data = self.load_data()
        updated_data = [item for item in data if item['title'].lower() != title.lower()]

        if len(updated_data) == len(data):
            print(f"Вакансия с заголовком '{title}' не найдена.")
        else:
            with open(self._filename, 'w', encoding='utf-8') as f:
                json.dump(updated_data, f, ensure_ascii=False, indent=4)


# Пример использования
handler = JSONFileHandler()

# Добавление новых вакансий
new_vacancies = [
    {"title": "Разработчик", "salary": 60000, "url": "http://example.com", "description": "Описание вакансии"},
    {"title": "Дизайнер", "salary": 50000, "url": "http://example.com", "description": "Описание вакансии"}
]
handler.save_data(new_vacancies)

# Загрузка данных
loaded_data = handler.load_data()
print("Загруженные данные:", loaded_data)

# Удаление вакансии
handler.delete_data("Разработчик")
print("Данные после удаления:", handler.load_data())
