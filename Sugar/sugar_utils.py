import json
import os

from typing import Any
from datetime import datetime


PathToFile = str
RealNumber = int | float


class SugarUtils:
    @staticmethod
    def write_json_file(obj: Any, path: PathToFile) -> None:
        folder, _ = os.path.split(path)

        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(path, mode="w", encoding="utf-8") as json_file:
            json.dump(obj, json_file, indent=4)
            print(f'File {path} has been written: {datetime.now().strftime("%d-%m %H:%M")}')

    @staticmethod
    def read_json_file(path: PathToFile) -> Any:
        if not os.path.exists(path):
            return []

        with open(path, encoding="utf-8") as json_file:
            print(f'File {path} has been read: {datetime.now().strftime("%d-%m %H:%M")}')
            return json.load(json_file)

    @staticmethod
    def try_to_int(number: RealNumber) -> RealNumber:
        number = float(number)

        if number.is_integer():
            return int(number)

        return number
