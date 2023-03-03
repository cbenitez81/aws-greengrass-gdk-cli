from pathlib import Path

from gdk.recipes.JsonRecipe import JsonRecipe
from gdk.recipes.Recipe import Recipe
from gdk.recipes.YamlRecipe import YamlRecipe


class RecipeFactory:
    def __init__(self):
        self.json = ".json"
        self.yaml = ".yaml"

    def get(self, file_path: Path) -> Recipe:
        if self._is_json(file_path):
            return JsonRecipe(file_path)
        elif self._is_yaml(file_path):
            return YamlRecipe(file_path)

    def _is_json(self, file_path: Path):
        return file_path.name.endswith(self.json)

    def _is_yaml(self, file_path: Path):
        return file_path.name.endswith(self.yaml)
