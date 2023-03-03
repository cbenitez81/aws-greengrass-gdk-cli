import json
from pathlib import Path

from gdk.recipes.Recipe import Recipe


class JsonRecipe(Recipe):
    def __init__(self, file_path: Path) -> None:
        super().__init__()
        self.file_path = file_path

    def load(self) -> dict:
        with open(self.file_path, "r", encoding="utf-8") as r_file:
            recipe = r_file.read()
            recipe_json = json.loads(recipe)
            return recipe_json

    def write(self, content) -> None:
        with open(self.file_path, "w", encoding="utf-8") as prf:
            prf.write(json.dumps(content, indent=4))
