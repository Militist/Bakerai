from abc import ABC, abstractmethod

class Bakery_products(ABC):
    def __init__(self, price, expiration_Date):
        self.list_Of_Ingredients
        self.price = price
        self.expiration_Date = expiration_Date

        @abstractmethod
        def getInfo(self):
            pass
