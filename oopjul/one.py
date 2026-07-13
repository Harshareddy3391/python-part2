from abc import ABC,abstractmethod


class Bank(ABC):
    @abstractmethod
    def m1(self):
        pass


a=Bank()
print(a)