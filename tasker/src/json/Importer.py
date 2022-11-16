import json


class Importer:

    def __init__(self):
        self._tasks = []
        self._file_name = "taski.json"

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open(self._file_name, "r", encoding='utf-8') as file:
            self._tasks = json.load(file)

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self._tasks