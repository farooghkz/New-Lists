class list(list):
    def last_index(self, V) -> int:
        #TODO: docstring
        new_self = self.copy()
        new_self.reverse()
        for i, v in enumerate(new_self):
            if v == V:
                return -(i - len(self) + 1)
        if type(val) == str:
            raise ValueError("\"" + V + "\"" + " is not in list")
        else:
            raise ValueError(V + " is not in list")

    def sub(self, L):
        #TODO: docstring
        if self == L:
            return 0
        if len(self) < len(L):
            return None

        for i, v in enumerate(self):
            if v == L[0]:
                if self[i:i + len(L)] == L:
                    return i
                else:
                    return None
        return None

    def del_sublist(self, L) -> None:
        #TODO: docstring
        if not L: return
        if type(L) is not list:
            raise ValueError(str(L) + " is not a list")
        index = self.sub(L)
        if index == None:
            raise ValueError(str(L) + ' is not a sublist of the list')

        for i in range(len(L)):
            del(self[index])

    def replace(self, V1, V2) -> None:
        #TODO: docstring
        for i, v in enumerate(self):
            if v == V1:
                self[i] = V2

