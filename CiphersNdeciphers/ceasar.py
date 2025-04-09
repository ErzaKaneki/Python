letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

secretMessage = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

def decipher(message, offset):
    newMessage = []
    message = message.lower()
    for char in message:
        if char in letters:
            base = letters.index(char)
            cipher = (base + offset) % 26
            newMessage.append(letters[cipher])
        else:
            newMessage.append(char)
    print(''.join(newMessage))

decipher(secretMessage, 10)

newMessage = "i was able to decode it, thank you for the fun challenge!"

def cipher(message, offset):
    secretMessage = []
    message = message.lower()
    for char in message:
        if char in letters:
            base = letters.index(char)
            decipher = (base - offset) % 26
            secretMessage.append(letters[decipher])
        else:
            secretMessage.append(char)
    print(''.join(secretMessage))

cipher(newMessage, 10)