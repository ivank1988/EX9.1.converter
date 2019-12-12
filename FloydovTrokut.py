broj_redaka = int(input("Enter the range: "))

for i in range(1, broj_redaka + 1):
    brojac = 1
    for broj_stupaca in range(1, i + 1):
        print(brojac, end=" ")
        brojac = 1 + brojac
    print()


