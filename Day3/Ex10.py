class Shelf:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


my_shelf = Shelf(["Book", "Pen", "Notebook"])

print(len(my_shelf))