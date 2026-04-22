from abc import ABC, abstractmethod



class Bank(ABC):


    @abstractmethod
    def Account(self):
        print("hello")
