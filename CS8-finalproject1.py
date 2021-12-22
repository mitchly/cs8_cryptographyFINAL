# Michelle Ly, for CMPSC 8, Fall 2020

'''
createAlphabet() returns a string with lowercase alphabet,
uppercase alphabet, and some additional symbols
(a space, a comma, a period, a hyphen('-'), 
and an exclamation point (!)).
'''
def createAlphabet():
    lowercase = "abcdefghijklmnopqrstuvwxyz" 
    uppercase = lowercase.upper()
    return lowercase + uppercase + " ,.-!" #returns concatenated string
'''
createCipherAlphabet(alphabet) takes in an alphabet, reverses it,
and replaces the first 10 existing digits with numbers 0 to 9. If
alphabet has less than 10 symbols in it, replace as many as possible
'''
def createCipherAlphabet(alphabet):
    cipher_alphabet = ""
    replaced = ""
    for character in alphabet: #reverses alphabet
        cipher_alphabet = character + cipher_alphabet
    i = 0
    while (i <= 9) and (i <= len(cipher_alphabet) - 1): #replaces first 10 digits with numbers 0-9
        replaced += str(i) #if length is less than 10 replace whatever existing characters
        i += 1
    if len(cipher_alphabet) > 10: #if length is more than 10 print out characters that aren't replaced
        replaced += cipher_alphabet[10:]
    return replaced
'''
subCipherEncode(plaintext, alphabet, cipher) takes in three string inputs:
a "plaintext" (statement that isn't coded yet), an alphabet, and a cipher alphabet.
The plaintext is converted into a ciphertext (coded statement).
'''
def subCipherEncode(plaintext, alphabet, cipher):
    ciphertext = ''
    if len(alphabet) != len(cipher): #if the length of alphabet is unequal to length of cipher, return -1
        return -1
    else:
        for character in plaintext: 
            index = alphabet.find(character)
            if index == -1: #if character in plaintext is not found in alphabet return None
                return None
            else: #if character in plaintext is found, find cipher character in same position and return
                  #ciphertext after iterating through all characters in plaintext
                ciphertext += cipher[index]
        return ciphertext
'''
subCipherDecode(ciphertext, alphabet, cipher) takes in three string inputs:
a "ciphertext" (a coded statement), an alphabet, and a cipher alphabet. The ciphertext
is decoded into a plaintext (a statement that isn't coded).
'''
def subCipherDecode(ciphertext, alphabet, cipher):
    plaintext = ''
    if len(alphabet) != len(cipher): #if the length of alphabet isn't the same as cipher, return -1
        return -1
    else:
        for character in ciphertext:
            index = cipher.find(character)
            if index == -1: #if character in ciphertext is not found in alphabet return None
                return None 
            else: #if character in ciphertext is found, find cipher characters in same position and  return
                  #plaintext after iterating through all characters in plaintext
                plaintext += alphabet[index]
        return plaintext
'''
getCharFwd(char, key) given a single character and key will return another
character in alphabet with a shifted position forward dependent upon the key.
'''
def getCharFwd(char, key):
    if type(key) != int: #if the key is not an int, return -1
        return -1
    elif key < 0: #if key is less than 0 return None
        return None
    elif len(str(char)) != 1: #if the length of char is not 1 return None
        return None
    else:
        index = createAlphabet().find(str(char)) 
        if index == -1: #if character is not in alphabet return None
            return None
        else: 
            index += key
            if index > len(createAlphabet()) - 1: #if the index goes over the index of the last character in
                                                  #createAlphabet(), use modulo to cycle back into the
                                                  #alphabet again
                return createAlphabet()[index % len(createAlphabet())]
            else:
                return createAlphabet()[index]
'''
getCharBack(char, key) given a single character and key will return another
character in alphabet with a shifted position backwards dependent upon the key.
'''
def getCharBack(char, key):
    if type(key) != int: #if the key is not an int, return -1
        return -1
    elif key < 0: #if key is less than 0 return None
        return None
    elif len(str(char)) != 1: #if the length of char is not 1 return None
        return None
    else:
        index = createAlphabet().find(str(char))
        if index == -1: #if character is not in alphabet return None
            return None
        else:
            index -= key #because the position goes backwards, the key is subtracted from the index
            if -index > len(createAlphabet()) - 1:
                    if (-index % len(createAlphabet())) == 0:
                    #this statement specifically checks if (-index % len(createAlphabet())) is equivalent to 0
                    #to print createAlphabet()[0] because the statement
                    #[len(createAlphabet()) - (-index % len(createAlphabet()))] doesn't cover it
                        return createAlphabet()[0]
                    else: #if (-index % len(createAlphabet())) == 0 is not true, it returns a shifted
                          #character based off of the given key (cycles back into the alphabet using modulo 
                          #because the number is greater than the length)
                        return createAlphabet()[len(createAlphabet()) - (-index % len(createAlphabet()))]
            else:
                return createAlphabet()[index]
'''
encryptWithCaesar(plainText, key) takes a string named plainText
and a key and returns a cipherText by shifting each character forward
by the given key. If the key given is negative, shift each character
backwards.
'''
def encryptWithCaesar(plainText, key):
    cipherText = ""
    if type(key) != int: #if the key is not an int, return None
        return None
    elif type(plainText) != str: #if the plainText is not a str, return None
        return None
    elif len(plainText) <= 0: #if the length of plainText is equal and less than 0, return None
        return None
    elif len(plainText) == 1: 
        if key > 0:
            return getCharFwd(plainText, key)
        else: #call getCharBack if it's a negative key
            return getCharBack(plainText, -key)
    else: 
        for character in plainText:
            index = createAlphabet().find(str(character))
            if index == -1: #if character is not in alphabet return None
                return None
            elif key > 0: #if the key is positive, call getCharFwd and shift each character forward based
                          #on the key
                cipherText += getCharFwd(character, key) 
            else: #if the key is negative, call getCharBack and shift each character backwards based on
                  #the key
                cipherText += getCharBack(character, -key)
        return cipherText
'''
decryptWithCaesar(cipherText, key) takes a string named cipherText
and a key and returns a plainText by shifting each character backward
by the given key. If the key given is negative, shift each character
forward.
'''
def decryptWithCaesar(cipherText, key):
    plainText = ""
    if type(key) != int: #if the key is not an int, return None
        return None
    elif type(cipherText) != str: #if the cipherText is not a str, return None
        None
    elif len(cipherText) <= 0: #if the length of plainText is equal and less than 0, return None
        return None
    elif len(cipherText) == 1:
        if key > 0: 
            return getCharBack(cipherText, key)
        else: #call getCharFwd if the key is negative
            return getCharFwd(cipherText, -key)
    else: 
        for character in cipherText:
            index = createAlphabet().find(str(character))
            if index == -1: #if character is not in alphabet return None
                return None
            elif key > 0: #if the key is positive, call getCharBack and shift each character backwards
                          #based on the key
                plainText += getCharBack(character, key)
            else: #if the key is negative call getCharFwd and shift each character forwards based on the key
                plainText += getCharFwd(character, -key)
        return plainText

'''
Docstrings in getCharFwd and getCharBack say
to return -1 when key is not a string
    
For the two Caesar cipher functions, it is stated to "apply
what you have learned above to ensure that your functions
don't do anything (i.e., return None) if an incorrect input
is given (e.g., if key is not an integer)."
'''
