human_years = float(input("Enter human years: "))
if human_years < 0:
    print("Error. Please enter a positive number.")
else:
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 21 + (human_years - 2) * 4
    print("The dog years is",dog_years)