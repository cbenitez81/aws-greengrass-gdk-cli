from pathlib import Path


class File:
    encoding = "utf-8"
    json = ".json"
    yaml = ".yaml"

    @classmethod
    def read(cls, file_path) -> str:
        with open(file_path, "r", encoding=cls.encoding) as file:
            return file.read()

    @classmethod
    def write(cls, file_path, content) -> None:
        with open(file_path, "w", encoding=cls.encoding) as file:
            file.write(content)

    @classmethod
    def is_json(cls, file_path: Path) -> bool:
        return file_path.name.endswith(cls.json)

    @classmethod
    def is_yaml(cls, file_path: Path) -> bool:
        return file_path.name.endswith(cls.yaml)
