class Node(Object):

    def _init_(self, initdata):
        self.data = initdata
        self.next= None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.set_next = new_next

    def _str_(self):
        return (str(self.data))

class Linkedlist(self, )
