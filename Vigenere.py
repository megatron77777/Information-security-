def vigenere_encryption(plainText, key):
    cipherText = ""
    plainText = plainText.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    n = 26
    key_len = len(key)
    
    for i in range(len(plainText)):
        p_char = plainText[i]
        
        k_char = key[i % key_len]
        
        p_idx = ord(p_char) - ord('A')
        k_idx = ord(k_char) - ord('A')
        
        c_idx = (p_idx + k_idx) % n
        
        c_char = chr(c_idx + ord('A'))
        cipherText += c_char
            
    return cipherText
