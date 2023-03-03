import json

from gdk.common.file_utils.File import File


class JsonFile:
    def __init__(self, file_path):
        self.file_path = file_path
        if not self._is_valid():
            raise Exception("Please provide a valid JSON file")

    def loads(self) -> dict:
        content = File.read(self.file_path)
        return json.loads(content)

    def dumps(self, content) -> None:
        json_content = json.dumps(content, indent=4)
        File.write(json_content)

    def _is_valid(self):
        return File.is_json(self.file_path)
