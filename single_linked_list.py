class Node(Object):

    def _init_(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.set_next = new_next

    def _str_(self):
        return (str(self.data))
