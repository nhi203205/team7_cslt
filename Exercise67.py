sum=0
while True:
  age=input("Please enter the age of Group members one by one \nNote: If no more member available please press ENTER key: ")
  if age=="":
      break
  else:
      age_int=int(age)
      if age_int < 2:
          sum=sum+0
      elif age_int>3 and age_int<13:
          sum=sum+14
      elif age_int>14 and age_int<65:
          sum=sum+23
      else:
          sum=sum+18
print("The total fair of your group is",round(sum,2))