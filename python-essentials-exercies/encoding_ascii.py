def encodeString(stringVal):
    encodedLists = []
    previousChar = stringVal[0]
    counter = 0
    for char in stringVal:
        if previousChar != char:
            encodedLists.append((previousChar, counter))
            counter = 0
        previousChar = char
        counter += 1
    encodedLists.append((previousChar, counter))
    return encodedLists

def decodeString(encodedList):
    decodeString = ""
    for key, value in encodedList:
        decodeString += key * value
    return decodeString

encoded = encodeString("AAAAABBBBCCC")
print(encoded)
print(decodeString(encoded))

encoded = encodeString("Booking")
print(encoded)
print(decodeString(encoded))