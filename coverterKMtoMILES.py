print("This is converter between km and miles")


while True:

    kilometer = int(input("unesi broj km: "))

    mile = 1.61 * kilometer

    print(str(kilometer) + " kilometers = " + str(mile) + " miles")

    upit = int(input("do you want another try (yes=1/no=0): "))

    if upit == 0:
        break
else:
    print ("goodbye")


