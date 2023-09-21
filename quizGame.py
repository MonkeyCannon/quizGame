import time

# Creating the intro
print("I wanna play a game....")
time.sleep(2)
print("I will ask you 5 questions...")
time.sleep(2)
print("If you manage to answer them all correctly, you are free to go...")
time.sleep(2)
print("But if you fail on a single one... you will die...")
time.sleep(2)
print("Let's begin...")
time.sleep(2)

questionRight = 0

#First question
firstQuestion = input("What is the capital of Norway? ")
firstQuestion = firstQuestion.lower()
if firstQuestion == "oslo":
    questionRight += 1
    print("Hm.. Next question...")
    time.sleep(2)
else:
    print("I see... Next question...")
    time.sleep(2)

#Second question
print("How many league titles has Liverpool won?")
print("A: 18")
print("B: 19")
print("C: 20")
secondQuestion = input("Choose A, B or C: ")
secondQuestion = secondQuestion.lower()
if secondQuestion == "b":
    questionRight += 1
    print("Aha...")
    time.sleep(2)
else:
    print("Hm... Okay...")
    time.sleep(2)

#Third question
print("What is the name of the main character in the game 'The Witcher 3'?")
print("A: Geralt")
print("B: Garelt")
print("C: Geraldo")
thirdQuestion = input("Choose A, B or C: ")
thirdQuestion = thirdQuestion.lower()
if thirdQuestion == "a":
    questionRight += 1
    print("Intresting...")
    time.sleep(2)
else:
    print("So thats your answer then... I see...")
    time.sleep(2)

#Fourth question
print("Question number 4...")
time.sleep(2)
print("How many minutes are there in a day?")
print("A: 1440")
print("B: 144")
print("C: 1400")
fourthQuestion = input("Choose A, B or C: ")
fourthQuestion = fourthQuestion.lower()
if fourthQuestion == "a":
    questionRight += 1
    print("Hm...")
    time.sleep(2)
else:
    print("Well well...")
    time.sleep(2)

#Fifth question
print("Last question...")
time.sleep(2)
fifthQuestion = input("How many bones are there in the human body? ")
if fifthQuestion == "206":
    questionRight += 1
    print("...")
    time.sleep(2)
else:
    print("Aha...")
    time.sleep(2)

#Final result
if questionRight == 5:
    print("So the final results are in...")
    time.sleep(2)
    print("You answered all the questions correctly...")
    time.sleep(2)
    print("You are free to go...")
    time.sleep(2)
    print("FOR NOW....")
    quit()
else:
    print("So the final results are in...")
    time.sleep(2)
    print("You answered " + str(questionRight) + " questions correctly...")
    time.sleep(2)
    print("How pathetic...")
    time.sleep(2)
    print("Get ready for agony...")
    time.sleep(2)
    print("For you will die... Slowly...")
    time.sleep(10)
    quit()
