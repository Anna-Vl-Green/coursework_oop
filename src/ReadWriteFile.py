from abc import ABC, abstractmethod


class ReadWriteFile(ABC):

    def read_file(self):
        pass

    def write_file(self, json_text):
        pass
