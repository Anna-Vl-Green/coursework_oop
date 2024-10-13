from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def __init__(self, file_worker):
        pass

    def load_vacancies(self, keyword):
        pass
