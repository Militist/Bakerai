class Shop:

    def __init__(self):
        self.my_dict = {}
    def order_formation(self, my_dict):
        while True:
            user_input = input("Введите название нужного товара и его количество через пробел:\n")
            if user_input == "стоп":
                break
            else:
                try:
                    string, number = user_input.split()
                    my_dict[string] = int(number)
                except ValueError:
                    print("Некоррктный ввоод. Необходимо ввести сроку и число через пробел!")
                    continue
            print(f"Сформированный список товаров и его количества:", my_dict)
            return my_dict