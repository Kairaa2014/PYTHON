

Marks1 = 94.4                                            
Marks2 = 87.4
Marks3 = 95.2
Marks4 = 66.4
Marks5 = 45.1

Marks = [Marks1,Marks2,Marks3,Marks4,Marks5]             
print(Marks)                                             
print(type(Marks))                                       
print(len(Marks))                                       
print(Marks[0])                                          

Marks[0] = 96                                    # List = Mutable, String = immutable    
print(Marks)


# LIST methods 


Marks.append(2)  
# addition to a list is called append

Marks.sort()
#sorting for ascending

Marks.sort(reverse = True)
#sorting for descending

Marks.reverse()
# reversing the order of the list ( without sorting )
 
Marks.remove(45.1)
# to remove something from the list

Marks.pop(3)
# to remove a specific index number

print(Marks)



# Tuples     

tuple = ("Kairaa",85,"TKPS")
print(tuple)
print(type(tuple))      
print(tuple[0])                   # Tuples are indexed in a different manner ( not by letters )
#tuple(0) = 5                     # Tuples = immutable
tuple = ( )                       # empty tuple
print(tuple)