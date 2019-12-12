print("This is converter between km and miles")

kilometer = int(input("unesi broj km: "))

mile = 1.61 * kilometer

print (str(kilometer) + " kilometers = " + str(mile) + " miles")

upit = int(input("do you want another try (yes=1/no=0): "))

while upit == 1:
    kilometer = int(input("unesi broj km: "))
    print(str(kilometer) + " kilometers = " + str(mile) + " miles")

else:
    print ("goodbye")


