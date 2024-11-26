import json
from typing import List, Dict


def load_json_file(filename: str) -> List[Dict]:
    """Загружает данные из JSON-файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_json_file(filename: str, data: List[Dict]) -> None:
    """Сохраняет данные в JSON-файл."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def is_duplicate(data: List[Dict], title: str) -> bool:
    """Проверяет наличие дубликата по заголовку вакансии."""
    return any(item['title'] == title for item in data)
