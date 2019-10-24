#This program is used to create a pascal triangle of a certain height.
#Each row is stored in a master list which is a list of lists, 
#with each row being a list,the master list is printed
#all on one line and then line by line and centered
#to look like a triangle
#Authour : Sam Hearne
#Date : 24/10/19
#Compiler : onlinegdb



#function which takes in the previous row (old_row) 
#and creates the row that will be after that
def make_new_row(old_row):
    
    
    #this starts the new row off at 1
    new_row = [1]
    x = len(old_row)
    x -= 1
    i=0
    y = 1
    
    
    #if the old_row is empty this will return 1 as the first row
    if len(old_row) == 0:
        new_row = [1]
        
        return new_row
    
    
    
    #if the old row only contains 1 this will return 1,1 as the second row
    if old_row[0] == 1 and len(old_row) ==1:
        new_row = [1,1]
        return new_row
    
    
    #if the first two rows are complete this will make the remaining rows
    #one row per function call
    while i < x:
        new_row.append(old_row[i]+old_row[y]) 
        
        i += 1
        y +=1
      
      
    #this ends the new row off at 1 
    new_row.append(1)
    return new_row
        
        

#Asking the user how high they want their triangle
#first row will always be 1 , the second row will always be 1,1
#the master list will be a list of lists, each row will be a list
old_row= []
master_list = []
height = int(input('Please enter your desired height'))     
x= int(0)




#this calls the function height(user's input) amount of times
while height > x:
    old_row= make_new_row(old_row)
    height -= 1
    master_list.append(old_row)



#This prints the master list all on one line
print(master_list)
x= len(master_list)
i = int(0)



#this prints the master list line by line so it 
#looks more like a pascal triangle
#each line is also centered at 100
#i forgot how to remove the comas and square brackets,sorry
while x > 0:
    
    print(''.join(str(master_list[i])).center(100))
    
    x-=1 
    i+=1
  
  
  
  
  
  
  
  
  
        