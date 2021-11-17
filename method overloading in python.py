"""
Can we do method overloading in Python?
Python does not support method overloading like Java or C++. We may overload the methods, but we can only use the latest defined method."""
class moloding:
    def add(self):
        a=10
        b=20
        print(a,b)
    def add(self,a,b):
        print(a,b)
obj=moloding()
obj.add()
"""TypeError: add() missing 2 required positional arguments: 'a' and 'b'"""
