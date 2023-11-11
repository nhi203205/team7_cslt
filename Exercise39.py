Decibel_level=float(input("Enter the sound level in decibels: "))
if Decibel_level == 130:
    print("Jackhammer")
elif Decibel_level == 106:
    print("Gas lawnmower")
elif Decibel_level == 70:
    print("Alarm clock")
elif Decibel_level == 40:
    print("Quiet room")
elif Decibel_level > 130:
    print("The sound level is higher than the loudest noise in the table")
elif 40 < Decibel_level < 70 :
    print("The sound level is between Quiet room and Alarm clock")
elif 70 < Decibel_level < 106:
    print("The sound level is between Alarm clock and Gas lawnmower")
elif 106 < Decibel_level < 130:
    print("The sound level is between Gas lawnmower and Jackhammer")
else:
    print("The sound level is lower than the quietest noise in the table")