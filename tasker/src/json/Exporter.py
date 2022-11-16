import json


class Exporter:

    def __init__(self):
        self._file_name = "taski.json"

    def save_tasks(self, tasks):
        # TODO zapisz taski do pliku tutaj
        with open(self._file_name, "w", encoding='utf-8') as file:
            json.dump(tasks, file, indent=4)
