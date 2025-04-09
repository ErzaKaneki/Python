letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

secretMessage = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"

def vDecipher(message, keyword):
    newMessage = []
    kwLength = len(keyword)
    message = message.lower()
    keyword = keyword.lower()
    i = 0
    for char in message:
        if char in letters:
            base = letters.index(char)
            kwOffset = letters.index(keyword[i % kwLength])
            i += 1
            cipher = (base + kwOffset) % 26
            newMessage.append(letters[cipher])
        else:
            newMessage.append(char)
    print(''.join(newMessage))

vDecipher(secretMessage, "friends")


myMessage = "this was a little more tricky, but i was able to get it!  thanks for another great challenge!"

def vCipher(message, keyword):
    newMessage = []
    keyword = keyword.lower()
    message = message.lower()
    keywordLength = len(keyword)
    i = 0
    for char in message:
        if char in letters:
            base = letters.index(char)
            kwOffset = letters.index(keyword[i % keywordLength])
            i += 1
            decipher = (base - kwOffset) % 26
            newMessage.append(letters[decipher])
        else:
            newMessage.append(char)
    return ''.join(newMessage)

    

encrypted = vCipher(myMessage, "code")
print(encrypted)

decrypted = vDecipher(encrypted, "code")
print(decrypted)