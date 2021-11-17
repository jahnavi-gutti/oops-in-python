"""
we can achieve method oveloding by usinf default keyword in python
"""
class molodingbydefault:
    def add(self ,a,b=500,c=100):        
        print(a+b+c)
  
obj=molodingbydefault()
obj.add(100)
obj.add(100,200)
obj.add(100,200,300)
"""

700
400
600"""
