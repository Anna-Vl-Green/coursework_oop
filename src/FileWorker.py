import json
import os
import config

from ReadWriteFile import ReadWriteFile


class FileWorker(ReadWriteFile):

    def __init__(self, filename=config.DATA_FILENAME, extension=config.DEFAULT_EXTENSION):
        os.mkdir(config.DATA_DIRECTORY)
        self.file_name = f'{filename}.{extension}'
        self.extension = extension
        self._check_extension()
        self.file_path = os.path.join(os.getcwd(), config.DATA_DIRECTORY, self.file_name)

    def _check_extension(self):
        match self.extension.lower():
            case 'json':
                pass
            case _:
                raise ValueError(f'Некорректное значение расширения файла: {self.extension}')

    def read_file(self) -> dict:
        if os.path.isfile(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as file:
                match self.extension.lower():
                    case 'json':
                        file_content = json.load(file)

            return file_content
        else:
            raise ValueError(f'Файл не существует: {self.file_path}')

    def write_file(self, json_text):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            match self.extension.lower():
                case 'json':
                    json.dump(json_text, file, ensure_ascii=False)
