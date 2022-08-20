'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import math
class nthpower:
    def __init__(self, x,n):
        self.n=n
        self.x=x
        
    def calculate(self):
        ans=pow(self.x,self.n)
        
        print(ans)
    
        
nthp = nthpower(10,2)
nthp.calculate()
