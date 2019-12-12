##this program can be used to create a vector (cartesian point) 
##and then add ,subtract, or multiply a point by a number , or by another point
##the program can also be used to find the magnitude of a point
##Throughout the code while adding subtracting etc q w e are used to repsent the xyz points of a new vector
##Compiler : onlinegdb
##date : 12/12/19
## Authour : Sam Hearne





##importing math for the sqrt function 
import math


##creating the class vector , x y and z represent points x y and z 
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z 
        
       
       
##defining the add method so it can be used to add two points together 
    def __add__(self,v2):
        
        q = v2.x + self.x
        w = v2.y +self.y  
        e = v2.z + self.z
        
        
        return 'x : {} y : {} z : {}'.format(q,w,e)
        
        
        
##defining the sub method so it can be used to subtract two points from each other     
    def __sub__(self,v2):
        
        q = self.x - v2.x
        w = self.y - v2.y  
        e = self.z - v2.z
        
        
        return 'x : {} y : {} z : {}'.format(q,w,e)
        
        
        
##defing the multiply method so it can be used to multiply  apoint by a number or by another point
    def __mul__(self,v2):
        
        
        if type(v2) != vector: 
            q = self.x * v2
            w = self.y * v2
            e = self.z * v2
            return 'x : {} y : {} z : {}'.format(q,w,e)
            
            
        else:
            q = v2.x * self.x
            w = v2.y * self.y  
            e = v2.z * self.z
            
            dot = q+w+e
            return 'Dot multiplication is : {}'.format(dot)
        
        
        
            
##Finding the magniute of a vector    
    def magnitude(self):
        added = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        return 'The magnitude is {}'.format(math.sqrt(added))
        
        
            
##defining str so the vector will be printed neatly in a readable fashion       
    def __str__(self):
        return 'x : {} y : {} z : {}'.format(self.x,self.y,self.z)







##start of main        
##creating classes , following the same additions subtractions etc that are show in the examples   
vector1 = vector(1.0,2.0,3.0)
vector2 = vector(5.0,5.0,5.0)
vector3 = vector1 + vector2
vector4 = vector1 - vector2
vector5 = vector1 * vector2
vector6 = vector1 * 2.0


##printing out the vectors and results of the additions ,subtractions etc
print(vector1)
print(vector2)
print (vector3)
print(vector4)
print(vector5)
print(vector6)
print (vector1.magnitude())