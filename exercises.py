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
print("###########################################################################")
#A tuple with 7 items and print it using a while loop.

# create the tupla
namesT= ("jacob", "Montserrat", "Erasmo", "Carlos", "Sofía","Max","Victor")
# create a counter and give it the value of "0"
counter= 0
#whit lean we know the length of the tuple
repeat= len(namesT)
#create the loop while and print the names
#while counter is less than the length of the tuple, it will print what is inside
while counter < repeat:
    print (namesT[counter])
    counter +=1
###########################################################################