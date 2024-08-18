# LESSON 1 - POOJA
""""""
a = 7//2  # division integer output
b = 7%2   # remainder division
print(str(a )+ "R"+str(b)) # concat variable integer
""""""

#LESSON  2- STRINGS
Name = 'M i C h A e L is nice'                           # string with single quotes and spaces allowed
Age = 10
UpperName = Name.upper()
LowerName = Name.lower()
print("Kairaa " + "is " + "10")                  # string + string - concat
print("answer is " + str(10+10))                 # string + integer - concat
print("He is " + str(Name))                      # string + string type variable - concat
print("He is " +str(Age))                        # string + integer type variable - concat
                                                 
print(Name[0])                                   # indexing name[0] - first character ; always starts with 0
print(Name[-1])                                  # indexing name[-1] - last character
print(len(Name))                                 # length of string
print(Name[0:4])                                 # slicing name[0:2] - 3 characters output
print (Name[::4])                                # stride selecting every second character - name[::2]
print(Name[0:5:2])                               # slice&stride - get every 2nd element from 0:4 and name[0:5:2]
print(3*"Michael")                               # print string 3 times - 3*michael 
print(3*Name)                                    # also print string 3 times with variable 

                                                 
   
print(UpperName)                                # string convert to upper case ; name.upper()
print(LowerName)                                # string convert to lower case ; name.lower()
print("Michael is \n nice!")                    # new line \n
print("Michael is \t nice!")                    # tab \t
Replace = Name.replace('nice','bad')            # replace Name michael to janet ; name.replace('michael','janet')  
print(Replace) 
Find = Name.find('nice')                        # find 'el' in michael ; name.find('el')                                  
print(Find)                                
Split = Name.split()                            # split string ; name.split(Name)
print(Split)


# LIST

var="Kairaa"                                    
var1 = var[0:2]                                # Slicing ( 0:2 ) Ans : index 0,1
print(var1)

var = "K air aa Sharma"                        # not working ( ask shweta maam)
var1 = var.strip()
print(var1)

var = "Kairaa,k"                               # var ( have to write which variable you want to split )
var1 = var.split(",")
print(var1)

var = "Kairaa is nice"                         # returns the index 
var1 = var.find("a")
print(var1)