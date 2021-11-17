class vehicle:
    def __init__(self,colour,maxspeed):
        self.colour=colour
        self.maxspeed=maxspeed
class car(vehicle):
    def __init__(self,colour,maxspeed,noofgears,isconvertable):
        super().__init__(colour,maxspeed)
        self.noofgears=noofgears
        self.isconvertable=isconvertable
    def print(self):
        print(self.colour,self.maxspeed,self.noofgears,self.isconvertable)
c=car("red",15,3,False)    
c.print()
#red 15 3 False
