note=input("Choose a note from C0 to C8: ")
word=note[0]
number=int(note[1])
if word=='C' or word=='D' or word=='E' or word=='F' or word=='G' or word=='A' or word=='B':
    if number<0 or number>8:
        print('Invalid note.')
    else:
        if word=='C':
            frequency = 261.63 / 2 ** (4 - number)
            print('The frequency of' ,note, 'is',frequency, 'Hz')
        elif word=='D':
            frequency = 293.66 / 2 ** (4 - number)
            print('The frequency of' ,note, 'is',frequency, 'Hz')
        elif word=='E':
            frequency = 329.63 / 2 ** (4 - number)
            print('The frequency of' ,note, 'is',frequency, 'Hz')
        elif word=='F':
            frequency = 349.23 / 2 ** (4 - number)
            print('The frequency of' ,note, 'is',frequency, 'Hz')
        elif word=='G':
            frequency = 392.00 / 2 ** (4 - number)
            print('The frequency of' ,note, 'is',frequency, 'Hz')
        if word=='A':
            frequency = 440.00 / 2 ** (4 - number)
            print('The frequency of' ,note, 'is',frequency, 'Hz')
        if word=='B':
            frequency = 493.88 / 2 ** (4 - number)
            print('The frequency of' ,note, 'is',frequency, 'Hz')
else: 
    print('Invalid note.')