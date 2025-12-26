def autokey_decryption(cipherText, key):
    plainText = ""
    cipherText = cipherText.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    n = 26
    
    keystream_current = key
    
    for i in range(len(cipherText)):
        c_char = cipherText[i]
        k_char = keystream_current[i]
        
        c_idx = ord(c_char) - ord('A')
        k_idx = ord(k_char) - ord('A')
        
        p_idx = (c_idx - k_idx) % n
        
        p_char = chr(p_idx + ord('A'))
        plainText += p_char
        
        keystream_current += p_char
            
    return plainText
