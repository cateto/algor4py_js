""" Character Input Solutions """

name = input("What is your name: " )
age = int(input("How old are you: "))
year = str((2014-age)+100)
print(name + " will be 100 years old in the year"+year)

""" Odd Or Even Solutions """

num = input("Enter a number: " )
mod = int(num) % 2
if mod > 0:
    print("You picekd an odd number.")
else:
    print("You picked an even number.")
    
    
#####

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
    
    
""" Divisors Solutions """

num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)

""" List Overlap Solutions """

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
overlap = set()

for i in a:
    for j in b:
        if i==j:
            overlap.add(i)
            
print(overlap)


""" String Lists Solutions """

word = input("Please enter a word : \n")
word = str(word)
reverser = word[::-1]
print(reverser)
if word == reverser:
    print("This word is a palindrome")
    
else :
    print("This word is not a palindrome")
    

###
    
def reverse(word):
    x =''
    for i in range(len(word)):
        x += word[len(word)-1-i]
    return x

word = input('give me a word:\n')
x = reverse(word)

if x == word:
    print("This word is a palindrome")
else :
    print("This word is not a palindrome")    