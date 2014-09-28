
def insert_naive(lst, thing):
    lst.append(thing)
    lst.sort()

def insert_slow(lst, thing):
    import time
    time.sleep(0.001)
    lst.append(thing)
    lst.sort()

insert_default = insert_naive

class Sorter1(object):
    def __init__(self, insertion_strategy=None):
        if insertion_strategy is None:
            insertion_strategy = insert_default
        self.insert = insertion_strategy
        self.lst = []

    def add(self, thing):
        "Adds a new element and then arranges for the lsit to be sorted again"
        self.insert(self.lst, thing)

    def as_list(self):
        "returns a sorted list at all times"
        return self.lst[:]


