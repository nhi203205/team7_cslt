string = input("Enter a string: ")
str=""
for i in range(len(string)):
    char = string[i]
    if ( 'A'<=char<='Z'):
        str+=str(chr(ord(char)+ord('a')-ord('A')))
    else:
        str=str+char
is_palindrome=True
left=0
right=len(string)-1
while left < right:
    if string[left] != string[right]:
        palindrome = False
        break
    left = left + 1
    right = right - 1
if is_palindrome==True:
    print(string,"is a palindrome.")
else:
    print(string,"is not a palindrome.")