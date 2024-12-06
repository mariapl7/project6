import json
from typing import List, Dict


def load_json_file(filename: str) -> List[Dict]:
    """Загружает данные из JSON-файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {filename}.")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка при загрузке файла {filename}: {e}")
        return []


def save_json_file(filename: str, data: List[Dict]) -> None:
    """Сохраняет данные в JSON-файл."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при записи в файл {filename}: {e}")


def is_duplicate(data: List[Dict], title: str) -> bool:
    """Проверяет наличие дубликата по заголовку вакансии."""
    if not isinstance(data, list):
        print("Ошибка: data должно быть списком.")
        return False
    if not isinstance(title, str):
        print("Ошибка: title должно быть строкой.")
        return False
    return any(item['title'] == title for item in data)
