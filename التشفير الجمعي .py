def encryption(plainText, key):
    cipherText = ""
    key = key % 26 
    
    for char in plainText:
        if 'A' <= char <= 'Z':
            idx = ord(char) - ord('A')
            cipher_idx = (idx + key) % 26
            cipherChar = chr(cipher_idx + ord('A'))
            cipherText += cipherChar
        else:
            cipherText += char
            
    return cipherText
