print("Welcome to data processing quiz!")

playing = input("Do you want to play?(yes/no) ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
count = 0

answer = input("What does CPU stand for? ")
count += 1
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1 #score = score + 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
count += 1
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
count += 1
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
count += 1
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does UPS stand for? ")
count += 1
if answer.lower() == "uninterrupted power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / count) * 100) + "%.")
