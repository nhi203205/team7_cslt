message = input('Are you encoding or decoding your message? ')
if message == 'encoding':
    message = input('Enter your message: ')
    letter = ''
    for word in message:
        if (word == 'A') or (word == 'a'):
            letter += 'D'
        elif (word == 'B') or (word == 'b'):
            letter += 'E'
        elif (word == 'C') or (word == 'c'):
            letter += 'F'
        elif (word == 'D') or (word == 'd'):
            letter += 'G'
        elif (word == 'E') or (word == 'e'):
            letter += 'H'
        elif (word == 'F') or (word == 'f'):
            letter += 'I'
        elif (word == 'G') or (word == 'g'):
            letter += 'J'
        elif (word == 'H') or (word == 'h'):
            letter += 'K'
        elif (word == 'I') or (word == 'i'):
            letter += 'L'
        elif (word == 'J') or (word == 'J'):
            letter += 'M'
        elif (word == 'K') or (word == 'k'):
            letter += 'N'
        elif (word == 'L') or (word == 'l'):
            letter += 'O'
        elif (word == 'M') or (word == 'm'):
            letter += 'P'
        elif (word == 'N') or (word == 'n'):
            letter += 'Q'
        elif (word == 'O') or (word == 'o'):
            letter += 'R'
        elif (word == 'P') or (word == 'p'):
            letter += 'S'
        elif (word == 'Q') or (word == 'q'):
            letter += 'T'
        elif (word == 'R') or (word == 'r'):
            letter += 'U'
        elif (word == 'S') or (word == 's'):
            letter += 'V'
        elif (word == 'T') or (word == 't'):
            letter += 'W'
        elif (word == 'U') or (word == 'u'):
            letter += 'X'
        elif (word == 'V') or (word == 'v'):
            letter += 'Y'
        elif (word == 'W') or (word == 'w'):
            letter += 'Z'
        elif (word == 'X') or (word == 'x'):
            letter += 'A'
        elif (word == 'Y') or (word == 'y'):
            letter += 'B'
        elif (word == 'Z') or (word == 'z'):
            letter += 'C'
        else:
            letter += word
    print('Encoding result:',letter)
else:
    message = input('Enter your message: ')
    letter = ''
    for word in message:
        if (word == 'A') or (word == 'a'):
            letter += 'X'
        elif (word == 'B') or (word == 'b'):
            letter += 'Y'
        elif (word == 'C') or (word == 'c'):
            letter += 'Z'
        elif (word == 'D') or (word == 'd'):
            letter += 'A'
        elif (word == 'E') or (word == 'e'):
            letter += 'B'
        elif (word == 'F') or (word == 'f'):
            letter += 'C'
        elif (word == 'G') or (word == 'g'):
            letter += 'D'
        elif (word == 'H') or (word == 'h'):
            letter += 'E'
        elif (word == 'I') or (word == 'i'):
            letter += 'F'
        elif (word == 'J') or (word == 'J'):
            letter += 'G'
        elif (word == 'K') or (word == 'k'):
            letter += 'H'
        elif (word == 'L') or (word == 'l'):
            letter += 'I'
        elif (word == 'M') or (word == 'm'):
            letter += 'J'
        elif (word == 'N') or (word == 'n'):
            letter += 'K'
        elif (word == 'O') or (word == 'o'):
            letter += 'L'
        elif (word == 'P') or (word == 'p'):
            letter += 'M'
        elif (word == 'Q') or (word == 'q'):
            letter += 'N'
        elif (word == 'R') or (word == 'r'):
            letter += 'O'
        elif (word == 'S') or (word == 's'):
            letter += 'P'
        elif (word == 'T') or (word == 't'):
            letter += 'Q'
        elif (word == 'U') or (word == 'u'):
            letter += 'R'
        elif (word == 'V') or (word == 'v'):
            letter += 'S'
        elif (word == 'W') or (word == 'w'):
            letter += 'T'
        elif (word == 'X') or (word == 'x'):
            letter += 'U'
        elif (word == 'Y') or (word == 'y'):
            letter += 'V'
        elif (word == 'Z') or (word == 'z'):
            letter += 'W'
        else:
            letter += word
    print('Decoding result:',letter)
print('Encrypted successfully!')