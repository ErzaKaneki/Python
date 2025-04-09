letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

secretMessage = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

def decipher(message, offset):
    newMessage = []
    for letter in message:
        if letter in letters:
            base = letters.index(letter)
            cipher = base + offset
            x = cipher % 26
            newMessage.append(letters[x])
        else:
            newMessage.append(letter)
    print(''.join(newMessage))

decipher(secretMessage, 10)

newMessage = "i was able to decode it, thank you for the fun challenge!"

def cipher(message, offset):
    secretMessage = []
    for letter in message:
        if letter in letters:
            base = letters.index(letter)
            decipher = base - offset
            x = decipher % 26
            secretMessage.append(letters[x])
        else:
            secretMessage.append(letter)
    print(''.join(secretMessage))

cipher(newMessage, 10)