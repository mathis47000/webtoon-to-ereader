# services/storage.py
import os, json
from typing import Any

LIST_FILE_PATH = os.path.join(os.path.dirname(__file__), '../data/list.json')

def load_json() -> Any:
    if os.path.exists(LIST_FILE_PATH):
        with open(LIST_FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_json(data: Any) -> None:
    with open(LIST_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
