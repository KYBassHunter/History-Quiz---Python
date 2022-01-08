print("History Quiz!")

playing = input("Do you want to play a game? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Who was President during the Civil War? ")
if answer == "Abraham Lincoln":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who was the third President of the United States? ")
if answer == "Thomas Jefferson":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("President during Iran-Contra? ")
if answer == "Ronald Reagan":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who was President on 9/11? ")
if answer == "George Bush":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")