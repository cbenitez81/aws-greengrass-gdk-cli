from pathlib import Path

import yaml

from gdk.recipes.Recipe import Recipe


class YamlRecipe(Recipe):
    def __init__(self, file_path: Path) -> None:
        super().__init__()
        self.file_path = file_path

    def load(self) -> dict:
        with open(self.file_path, "r", encoding="utf-8") as r_file:
            content = r_file.read()
            recipe_yaml = yaml.safe_load(content)
            return recipe_yaml

    def write(self, content) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file:
            yaml.dump(content, file)
