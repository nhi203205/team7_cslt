def square_root(number):
    epsilon = 0.01
    k       = number
    guess   = k / 2
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (guess ** 2 - k) / (2 * guess)
    return guess
x= int(input('Input number: '))
sqroot_number = square_root(x)
print ('The square root of', x,'is',round(sqroot_number,2))