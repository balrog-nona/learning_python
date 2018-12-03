volba = int(input("Do you wanna count price or nutritients? 1/2: "))
program = True
while program == True:
    if volba == 1:
        cena_baleni = float(input("\nEnter the price of the package in Kc: "))
        vaha_baleni = float(input("Enter the weight of the package in grams: "))
        vaha_porce = float(input("Enter the weight of your portion in grams: "))
        postovne = 0
        chci = input("Do you wanna include shipping into the price? y/n: ")
        if chci == "y":
            postovne = float(input("Enter the shipping price in Kc: "))
        cena_drinku = (cena_baleni + postovne) / vaha_baleni * vaha_porce
        print("Your drink costs: ", cena_drinku)
        opet = input("\nDo you wanna count the price again? y/n: ")
        if opet == "y":
            volba = 1
        elif opet == "n":
            pokracovat = input("Do you wanna count nutritients? y/n: ")
            if pokracovat == "y":
                volba = 2
            else:
                print("The program is over.")
                program = False
    if volba == 2:
        kcal_deka = float(input("\nEnter kcal for 100g of protein: "))
        protein_deka = float(input("Enter proteins for 100g: "))
        vaha_porce = float(input("Enter the weight of your portion in grams: "))
        kcal_porce = kcal_deka / 100 * vaha_porce
        protein_porce = protein_deka / 100 * vaha_porce
        print("Your portion contains: \n", kcal_porce, " kcal \n", protein_porce, "g of proteins")
        opet = input("\nDo you wanna count nutritients again? y/n: ")
        if opet == "y":
            volba = 2
        elif opet == "n":
            pokracovat = input("Do you wanna count a price? y/n: ")
            if pokracovat == "y":
                volba = 1
            else:
                print("The program is over.")
                program = False

