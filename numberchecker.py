state = 1

while state == 1:
    num = int(input("Skirv en siffra: "))

    if num > 0:
        print("positivt")

    elif num < 0:
        print ("negativt")

    state = int(input("Fortsätta? 1. Ja, 2. Nej: "))