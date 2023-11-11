frequency=float(input("Enter the frequency: "))
if abs(frequency - 261.63) <= 1:
    print("Name note is C")
elif abs(frequency - 293.66) <= 1:
    print("Name note is D")
elif abs(frequency - 329.63) <= 1:
    print("Name note is E")
elif abs(frequency - 349.23) <= 1:
    print("Name note is F")
elif abs(frequency - 392.00) <= 1:
    print("Name note is G")
elif abs(frequency - 440.00) <= 1:
    print("Name note is A")
elif abs(frequency - 493.88) <= 1:
    print("Name note is B")
else:
    print("The frequency does not correspond to a known note.")