print("Choose the name of month: January, February, March, April, May, June, July, August, September, October, November, December")
month=(input("The name of month: "))
if month=="February":
    print("Number of days: 28 or 29 days")
elif month=="April" or month=="June" or month=="September" or month=="November":
    print("Number of days: 30 days")
elif month=="January" or month=="March" or month=="May" or month=="July" or month=="August" or month=="October" or month=="December":
    print("Number of days: 31 days")
else:
    print("The name of month is incorrect.")