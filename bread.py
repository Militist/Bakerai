from bakery_products import Bakery_products
class Bread(Bakery_products):
    def __init__(self, price, expiration_Date):
        super().__init__(price, expiration_Date)

    def getInfo(self):
        print(f"Товар имеет следующие цену: {price} и срок годности: {expiration_Date}.")
