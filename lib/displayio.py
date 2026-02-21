class Group():
    def __init__(self):
        self.list = []
    
    def __getitem__(self, index):
        return self.list[index]
    
    def __setitem__(self, index, value):
        self.list[index] = value
    
    def append(self, value):
        self.list = self.list + [value]