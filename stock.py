from shop import Shop

class Stock:

    def __init__(self, my_dict):
        self.dict1 = {"буханка": 5, "батон": 7, "галета": 2, "калач": 3, "крендель": 4, "лаваш": 9, "сочень": 1}

    def __getitem__(self, key):
        return self.dict1[key]

    def __setitem__(self, key, value):
        self.dict1[key] = value

    def __delitem__(self, key):
        del self.dict1[key]

    def finding_The_Difference(self, dict1):
        diff = {}
        for key in dict1:
            if key in my_dict and dict1[key] != my_dict[key]:
                diff[key] = dict1[key] - my_dict[key]
        return diff