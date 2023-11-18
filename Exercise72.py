string=input("Enter a string: ")
count=len(string)
n=count//2
for i in range(n):
    if string[i]!=string[-1-i]:
        print("Not a palindrome")
        exit()
print("A palindrome")