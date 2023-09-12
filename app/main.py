class Dictionary(object):
    def __init__(self):
        self.dict_list = []

    def __setitem__(self, *args):
        if len(args) != 2:
            raise KeyError("Dictionary must have a key and a value")
            # print("Dictionary must have a key and a value")
            # return
        for index, _ in enumerate(self.dict_list):
            if _[0] == args[0]:
                self.dict_list[index] = (_[0], args[1])
                return
        self.dict_list.append((args[0], args[1]))

    def __getitem__(self, key) -> tuple:
        for _ in self.dict_list:
            if key == _[0]:
                return _[1]
        raise KeyError("key not found")

    def __len__(self):
        return len(self.dict_list)


# dictionary = Dictionary()
# dictionary["missing_key"]
# # dictionary.__setitem__("two")
# # # uuu = dictionary.__getitem__("two")
# yyy = 0
