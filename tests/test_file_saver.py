import unittest
import os
from src.file_saver import JSONFileHandler  # Предполагая, что у вас есть этот класс
from src.models import Vacancy  # Импортируем класс Vacancy


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
        data = [
            Vacancy(title='Разработчик', url='http://example.com', salary=60000, description='Разработка приложений')]
        self.handler.save_data(data)
        loaded_data = self.handler.load_data()
        expected_data = [vacancy.to_dict() for vacancy in data]
        self.assertEqual(loaded_data, expected_data)

    def test_delete_data(self):
        """Тестирует удаление данных из JSON-файла."""
        data = [
            Vacancy(title='Разработчик', url='http://example.com', salary=60000, description='Разработка приложений')]
        self.handler.save_data(data)

        # Удаляем вакансию
        self.handler.delete_data('Разработчик')

        # Проверяем, что файл пуст
        loaded_data = self.handler.load_data()
        self.assertEqual(loaded_data, [])


if __name__ == '__main__':
    unittest.main()
