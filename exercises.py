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
#2-A tuple with 7 items and print it using a while loop.

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
print("###########################################################################")
#3- A dictionary with 3 properties, modify any of those and print it.

#create the dictionary
dictionary= {"Erasmo":19,"carlos":18,"Jacob":18}
#here change the value of the age of the first value
newage=input("switch the age ")
dictionary["Erasmo"]=newage
#print the dictrionary whit the new value
print(dictionary)
###########################################################################
print("###########################################################################")
#4-A function named operation, that receives 3 params.

#create  the function
def operation(sign, firstNumber, secondNumber):

    # create if statements for each of the cases
    if sign == "1":
        result = firstNumber + secondNumber
    elif sign == "2":
        result = firstNumber - secondNumber
    elif sign == "3":
        result = firstNumber * secondNumber
    elif sign == "4":
        result = firstNumber / secondNumber
    else:
        result = None

    return result

#ask what operation want to perform and the values
sign = input("what operation do you want to do 1-addition, 2-subtraction, 3-multiplication, 4-division ")
number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))
#call the function and print the results
result_operation = operation(sign, number1, number2)
print("Resul of the operation:", result_operation)


