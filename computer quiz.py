

print ("welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("okay! lets play :)")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower()== "central processing unit":
    print('correct')
    score +=1
else:
    print("Incorrect! :(")

answer = input("what does GPU stand for ")
if answer.lower()== "graphics processing unit":
    print('correct')
    score +=1
else:
    print("Incorrect! :(")

answer = input("what does RAM stand for ")
if answer.lower()== "random access memory":
    print('wow.....correct')
    score +=1
else:
    print("Incorrect! :(")

answer = input("what does PSU stand for ")
if answer.lower()== "power supply":
    print('Amazing,,,,,correct')
    score +=1
else:
    print("Incorrect! :( ")

print("you are a champ you got"+str(score)+" questions correct!")
print("you got"+str((score/4)*100)+ "%")

print("Thank you the game ends here....:)")




