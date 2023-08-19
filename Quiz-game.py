print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Natural Satelite of Earth is? ")
if answer.upper() == "MOON":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("when India get their Independence? ")
if answer == "1947":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does UPI stand for? ")
if answer.lower() == "unified payment interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")    

print("" + str(score) + " questions are correct!") 
print("you got"  + str((score/5)*100) + "% marks.") 