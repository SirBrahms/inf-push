class LimList():
    def __init__(self, lst):
        self.inner_list = lst
    
    def check_new_element(self, e):
        if (self.inner_list.contains(e)):
            raise ValueError("Same Card Added Twice")
        else:
            self.inner_list.append(e)
    
    def append(self, e):
        self.inner_list.append(self.check_new_element(e))
            