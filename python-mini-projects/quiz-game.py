print('Welcome to My Computer quiz')

playing = input('do you want to play? ')

if playing.lower() != "yes":
  quit()

print("Okay! Let's play :)")

score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("i'm sorry you are incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
  print("Correct!")
  score += 1
else:
  print("i'm sorry you are incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
  print("Correct!")
  score += 1
else:
  print("i'm sorry you are incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
  print("Correct!")
  score += 1
else:
  print("i'm sorry you are incorrect!")

answer = input("Who invented tesla? ").lower()
if answer == "elon musk":
  print("Correct!")
  score += 1
else:
  print("i'm sorry you are incorrect!")

print('you got ' + str(score) + ' questions correct!')
print("you got " + str((score / 5)* 100) + "%.")