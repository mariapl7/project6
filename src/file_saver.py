from abc import ABC, abstractmethod
import json


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
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_data(self, data):
        """Сохраняет данные в JSON-файл, проверяя на дубликаты."""
        existing_data = self.load_data()
        titles = {item['title'] for item in existing_data}  # Множество заголовков
        for item in data:
            if item['title'] not in titles:  # Проверка на дубликаты
                existing_data.append(item)
                titles.add(item['title'])  # Добавляем заголовок в множество
        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)

    def delete_data(self, title):
        """Удаляет данные из JSON-файла по заголовку."""
        data = self.load_data()
        data = [item for item in data if item['title'] != title]  # Удаление по заголовку
        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


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
