x = 3
y = float(3)
# print(x,y)

values = [1,2.23,5,7,2,30,15]
# print(values)
for i in values:
    print(i)

    "test"
["t","e","s","t"]

x = "this is a thing"
y= x.split( ) #string to a list of strings (splits by the space here)
z = y[0] #1st word
# print(y)
# print(z)
# len(x) <- checks characters
# len(y) <- checks words
#.append adds to a list


#Using the "input" method in Python, ask a user to input a sentence. 
# Then develop a function that accepts a the user input and will tell you how many words are in that string. 
# First write out your plan in Pseudo-code using comments. Then craft the function.
# wrap int() around to turn string into integers
def countwords():
    words = input("give sentence") # asks user a question, input always a string
    word = words.split()
    print(len(word))
# countwords()

# odd or even function

def evenodd():
    number = input("give number")
    integer = (int(number) % 2)
    if integer == 1:
        print("this number is very odd")
    else:
        print("even")

# evenodd()

# Let's create a function to accept a "bill" value and offer a tip of 
# 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ".

def tips():
     ask =float(input("WHAT iS YOU BILL??????"))
     print("OK BUD")
     service = input("IS SERVICE bad, okay, good or great?")
     joop = service.lower().replace(" ", "")
     if joop=="bad":
         print(f"THE BILL IS${ask*1.25} and YOU SUCK")
     elif joop =="okay":
         print(f"THE BILL IS${ask*1.20} and you KINDA suck")
     elif joop == "good":
         print(f"The bill is${ask*1.15}, Thanks")
     elif joop == "great":
         print(f"Thanks, the bill is${ask*1}, You dont need tip lol")
     else:
         print(f"THAT WAS NOT ONE OF THE CHOICES, YOU BILL IS {ask*367836299999999999999321683686} AND YOU SUCK THE MOST")

# tips()

#Create a function that accepts an input and determines all factors of the number.

def factors():
    num = int(input("give me a number"))
    numbers = []
    for i in range(num):
        number = (num % (i+1))
        if number == 0:
            numbers.append(i+1)
    print(numbers)

    


def factorsGCF(num):
    numbers = []
    for i in range(num):
        number = (num % (i+1)) # finds remainder between number and 1 through the number
        if number == 0:
            numbers.append(i+1) # if no remainder, add to list
    print(numbers)

factorsGCF(88)
factorsGCF(100)
factorsGCF(8800)

# factorsGCF(50)
# Create a function that accepts 2 arguments. Find the greatest common factor between those numbers.

def gcf(num1, num2): 
    numbers1 = []
    numbers2 = []
    commonfactors = []
    for i in range(num1):        # get factors for 1
        number1 = (num1 % (i+1))     
        if number1 == 0:
            numbers1.append(i+1)
    for i in range(num2):        # get factors for 2
        number2 = (num2 % (i+1))
        if number2 == 0:
            numbers2.append(i+1)   
    for numb1 in numbers1:       # get common factors
        for i in range(len(numbers2)):
            if numb1 == numbers2[i]:
                commonfactors.append(numb1)
    if max(commonfactors) <= 0:
        print ("there has been a big eror")
        return()
    else:
        print (f"The GCF is {max(commonfactors)}")

# gcf(100,88)

def gcf2(num1, num2):
 commonfactor = []
 for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        commonfactor.append(i)
     

 print(f'The GCF is {max(commonfactor)}')

# gcf2(100,88)

def spaces(N,Y,T):
    for i in range(int(N)):
        if Y[i] == "." or T[i] == ".":
            N-=1
    print(f"GOOFY CREW WOBBLES {N} TIMES")

Yes = ["C","C",".","C","C"]
Tod = ["C","C",".",".","C"]

spaces(5,Yes,Tod)

def frenglish(Tx):
    numS = numT = 0
    lowTx = Tx.lower()
    for i in lowTx:
        if i == "s":
            numS += 1
        elif i == "t":
            numT += 1
    if numS >= numT:
        print("french")
    else:
        print("english")

cool = "The red cat sat on the mat. Why are you so sad cat? Don't ask that."
frenglish(cool)

def wizard(owner, N, duels):
    history=[]
    history.append(owner)
    for fights in duels:
        if fights[1] == owner:
            owner = fights[0]
            for i in range(len(history)):
                if history[i] != owner:
                    history.append(owner)
    print(owner)
    print(history)



wizard("A",3,["BA", "CB", "DA"])
wizard("N",5,["DA", "NB", "BA", "CD", "FA"])
wizard("X",4,["AX","BX","XA","DA"])