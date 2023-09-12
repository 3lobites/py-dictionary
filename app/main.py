class Dictionary(object):
    def __init__(self):
        self.dict_list = []

    def __setitem__(self, key, value):
        self.dict_list.append((key, value))

    def __getitem__(self, key) -> tuple:
        for _ in self.dict_list:
            if key == _[0]:
                return _[1]

    def __len__(self):
        return len(self.dict_list)


# test_dict = Dictionary()
# test_dict.__setitem__("two", 2222)
# uuu = test_dict.__getitem__("two")
# yyy = 0
