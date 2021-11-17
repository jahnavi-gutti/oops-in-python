from abc import ABC, abstractmethod   
class parent:
    def janu(self):
        pass
    @abstractmethod
    def tcs(self):
        pass

class child(parent):
    def tcs(self):
        print("child class")

c=child()
c.tcs()
#child class
