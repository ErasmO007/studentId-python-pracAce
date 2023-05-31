#1- A list with 5 items, add a new element and print it using a for loop.

#i create a list called names
names= ["jacob", "Montserrat", "Erasmo", "Carlos", "Sofía"]
#whit a input i ask a  for the new name
newName= input("Add a new name : ")
#Whit the append add a the new name to the end of the list
names.append(newName)
#in the loop "for" we print the list with all the elements
for name in names:
    print(name)
###########################################################################
