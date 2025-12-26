def autokey_encryption(plainText, key):
    cipherText = ""
    plainText = plainText.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    n = 26
    
    keystream_raw = key + plainText
    
    for i in range(len(plainText)):
        p_char = plainText[i]
        k_char = keystream_raw[i]
        
        p_idx = ord(p_char) - ord('A')
        k_idx = ord(k_char) - ord('A')
        
        c_idx = (p_idx + k_idx) % n
        
        c_char = chr(c_idx + ord('A'))
        cipherText += c_char
            
    return cipherText
