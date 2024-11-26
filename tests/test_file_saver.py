import unittest
import os
from src.file_saver import JSONFileHandler  # Предполагая, что у вас есть этот класс


class TestJSONFileHandler(unittest.TestCase):
    """Тестовый класс для проверки функциональности JSONFileHandler."""
    def setUp(self):
        """Создает экземпляр JSONFileHandler и задает имя файла для тестирования."""
        self.filename = "test_data.json"
        self.handler = JSONFileHandler(filename=self.filename)

    def tearDown(self):
        """Удаляет тестовый файл, если он существует."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_data(self):
        """Тестирует сохранение данных в JSON-файл и их загрузку."""
        data = [{'title': 'Разработчик', 'salary': 60000}]
        self.handler.save_data(data)
        loaded_data = self.handler.load_data()
        self.assertEqual(loaded_data, data)

    def test_save_duplicate_data(self):
        """Тестирует сохранение дублирующихся данных в JSON-файл."""
        data1 = [{'title': 'Разработчик', 'salary': 60000}]
        data2 = [{'title': 'Разработчик', 'salary': 70000}]  # Дубликат
        self.handler.save_data(data1)
        self.handler.save_data(data2)
        loaded_data = self.handler.load_data()
        self.assertEqual(len(loaded_data), 1)  # Проверка на уникальность

    def test_delete_data(self):
        """Тестирует удаление данных из JSON-файла."""
        data = [{'title': 'Разработчик', 'salary': 60000}]
        self.handler.save_data(data)
        self.handler.delete_data('Разработчик')
        loaded_data = self.handler.load_data()
        self.assertEqual(loaded_data, [])


if __name__ == '__main__':
    unittest.main()
