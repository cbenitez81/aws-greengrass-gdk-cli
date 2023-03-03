import yaml

from gdk.common.file_utils.files.File import File


class YamlFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def loads(self) -> dict:
        content = File.read(self.file_path)
        return yaml.safe_load(content)

    def dumps(self, content) -> None:
        yaml_content = yaml.dump(content)
        File.write(yaml_content)
