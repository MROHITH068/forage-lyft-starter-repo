from abc import ABC, abstractmethod

class Servicable:

    @abstractmethod
    def needs_service(self):
        pass