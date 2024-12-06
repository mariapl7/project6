import unittest
import os
from src.utils import load_json_file, save_json_file, is_duplicate


class TestUtils(unittest.TestCase):
    """Тестовый класс для проверки утилит, работающих с JSON-файлом."""
    def setUp(self):
        """Создает тестовые данные и сохраняет их в JSON-файл перед каждым тестом."""
        self.filename = "test_data.json"
        self.test_data = [{'title': 'Разработчик'}, {'title': 'Дизайнер'}]
        save_json_file(self.filename, self.test_data)

    def tearDown(self):
        """Удаляет тестовый файл после каждого теста."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_load_json_file(self):
        """Тестирует успешное загрузку данных из JSON-файла."""
        data = load_json_file(self.filename)
        self.assertEqual(data, self.test_data)

    def test_load_non_existent_file(self):
        """Тестирует загрузку данных из несуществующего файла, должен вернуть пустой список."""
        data = load_json_file("non_existent_file.json")
        self.assertEqual(data, [])

    def test_is_duplicate(self):
        """Тестирует проверку наличия дубликата по заголовку вакансии."""
        self.assertTrue(is_duplicate(self.test_data, 'Разработчик'))
        self.assertFalse(is_duplicate(self.test_data, 'Менеджер'))


if __name__ == '__main__':
    unittest.main()