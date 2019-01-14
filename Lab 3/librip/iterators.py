class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.unique=[]
        if len(kwargs) == 0:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs.values()
        pass

    def __next__(self):
        while True:
            item = self.items.__next__()
            if type(item) is str and self.ignore_case:
                myitem =item.lower()
            else:
                myitem = item
            if myitem not in self.unique:
                self.unique.append(myitem)
                return myitem
        pass

    def __iter__(self):
        return self
