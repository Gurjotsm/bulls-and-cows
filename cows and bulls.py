import random
import string
random_no_list = []
random_no_string = ""
random_no_list_1 = []
cows = 0
bulls = 0
a1 = []
length = 4
guesses = 0
while length != 0:
    random_no_list.append(random.choice(string.digits))
    length -= 1
for j in range(0,4):
    random_no_string = random_no_string + random_no_list[j]
print("hint : ",random_no_string)
length1 = len(random_no_string)
def cows_and_bulls(a):
    global cows
    global bulls
    global a1
    global length1
    global random_no_list_1
    for i in range(length1):
        if a[i] == random_no_list[i]:
            cows += 1
        else:
            a1.append(a[i])
            random_no_list_1.append(random_no_list[i])
    length2 = len(a1)
    for k in range(length2):
        if a1[k] in random_no_list_1:
            bulls += 1
            random_no_list_1.remove(a1[k])
        else:
            pass
    print("{} cows and {} bulls".format(cows,bulls))
    del a1
    del random_no_list_1
while True:
    user = list(input("Enter a 4 digit no: "))
    guesses += 1
    cows = 0
    bulls = 0
    cows_and_bulls(user)
    a1 = []
    random_no_list_1 = []
    if user == random_no_list:
        print("You guessed the no.! ")
        print("You took {} guesses".format(guesses))
        exit(0)