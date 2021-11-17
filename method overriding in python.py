#Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes.
class moverrriding:
    def transport(self):
        print("cycle")
class child(moverrriding):
    def transport(self):
        print("bike")
c=child()
c.transport()
    
#bike
