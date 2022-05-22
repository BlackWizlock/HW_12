from config import POST_PATH
from json import load as json_load
from json import dump as json_dump
from pprint import pprint as pp
from sys import getsizeof as gs
from re import findall


class DataBase:
    def __init__(self, path: str = POST_PATH):
        self.path = path
        self.data = []

    def __repr__(self) -> str:
        return f"БД: {self.path}\nСодержит записей: {len(self.data)}\nРазмер БД: {gs(DataBase)} Байт"

    def _json_loader(self) -> list:
        with open(self.path, 'r', encoding='utf-8') as f:
            return json_load(f)

    def json_write(self, data_to_write):
        database = self._json_loader()
        database.append(data_to_write)
        with open(self.path, 'w', encoding="utf-8") as f:
            json_dump(database, f, ensure_ascii=False, indent=2)

    def class_database_loader(self) -> None:
        for line in self._json_loader():
            self.data.append(line)

    def search_in_database(self, query: str) -> list:
        output_data = []
        for line in self.data:
            if query.lower().strip() in findall(r"\w+", line["content"].lower()):
                output_data.append(line)
        return output_data

# database = DataBase()
# database.class_database_loader()
# pp(len(database.data))
# pp(database.data)
# pp(database)
# pp(database.search_in_database("Утром"))
