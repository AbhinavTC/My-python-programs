class parent():
    def __init__(self):
        self.value = "Inside parent"


    def show(self):
      print(self.value)


class Child(parent):

    def __init__(self):
        self.value = "Inside child"

    def show(self):
        print(self.value)


obj1 = parent()
obj2 = Child()
obj2.show()
obj1.show()
