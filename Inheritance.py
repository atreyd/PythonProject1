class Parent:
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructer")

    def parentMethod(self):
        print("Calling parent method")

    def setattr(self, attr):
        Parent.parentAttr = attr

    def getattr(self):
        print("Parent Attribute ", Parent.parentAttr)


class Child(Parent):
    def __init__(self):
        print("Calling child constructer")


    def childMethod(self):
        print("Calling child method")


c = Child()
c.childMethod()
c.parentMethod()
c.setattr(500)
c.getattr()




