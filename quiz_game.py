print('Welcome to the Game!')

playing = input("Do you want to play? ")

if playing.lower() == "no":
    quit()

if playing.lower() != "yes":
    print("Invalid entry")
    quit()

print("Okay! lets play :)")
score = 0

answer = input("How many continents do we have? ")

if answer.lower() == "7":
    print("That's correct :)")
    score += 1
else:
    print("That is wrong :(")

answer = input("What continent is Russia in? ")

if answer.lower() == "europe and asia":
    print("That's correct :)")
    score += 1
else:
    print("Trick question :0 it's in two continents at once")

# The score needs to converted to string because
# if it remains an int the print looks like
# "you got + 1 + points" (Doesn't make sense/adding num to str)
# That's why we convert before doing anything else.
print("\nYou got " + str(score) + " point(s)")
print("You got " + str((score/2) * 100) + "%")