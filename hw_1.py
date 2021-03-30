class CustomList(list):
    """docstring"""

    def __sub__(self, other):
        new_self = CustomList(self)
        new_other = other[:]
        if len(self) > len(other):
            new_other.extend([0 for i in range(abs(len(self) - len(other)))])
        else:
            new_self.extend([0 for i in range(abs(len(self) - len(other)))])
        for i in range(len(new_self)):
            new_self[i] -= new_other[i]
        return new_self

    def __rsub__(self, other):
        new_self = CustomList(self)
        new_other = other[:]
        if len(self) > len(other):
            new_other.extend([0 for i in range(abs(len(self) - len(other)))])
        else:
            new_self.extend([0 for i in range(abs(len(self) - len(other)))])
        for i in range(len(new_self)):
            new_other[i] -= new_self[i]
        return new_other

    def __add__(self, other):
        new_self = CustomList(self)
        new_other = other[:]
        if len(self) > len(other):
            new_other.extend([0 for i in range(abs(len(self) - len(other)))])
        else:
            new_self.extend([0 for i in range(abs(len(self) - len(other)))])
        for i in range(len(new_self)):
            new_self[i] += new_other[i]
        return new_self

    def __radd__(self, other):
        return self + other

    def __lt__(self, other):
        if sum(self) < sum(other):
            return True
        return False

    def __le__(self, other):
        if sum(self) <= sum(other):
            return True
        return False

    def __ge__(self, other):
        if sum(self) >= sum(other):
            return True
        return False

    def __gt__(self, other):
        if sum(self) > sum(other):
            return True
        return False

    def __eq__(self, other):
        if sum(self) == sum(other):
            return True
        return False

    def __ne__(self, other):
        if sum(self) != sum(other):
            return True
        return False
