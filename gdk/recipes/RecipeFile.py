from pathlib import Path

from gdk.common.file_utils.File import File
from gdk.common.file_utils.JsonFile import JsonFile
from gdk.common.file_utils.YamlFile import YamlFile


class RecipeFile:
    json = ".json"
    yaml = ".yaml"

    def __init__(self, file_path: Path):
        self._file = self._get_recipe_file(file_path)

    def to_file(self, content) -> dict:
        self._file.dumps(content)

    def to_json(self) -> None:
        self._file.loads()

    def _get_recipe_file(self, file_path: Path):
        if File.is_json(file_path):
            return JsonFile(file_path)
        elif File.is_yaml(file_path):
            return YamlFile(file_path)
