def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def multiplicative_decryption(cipherText, key):
    plainText = ""
    n = 26
    
    try:
        k_inv = mod_inverse(key, n)
    except:
        return "" 
    
    for char in cipherText:
        if 'A' <= char <= 'Z':
            idx = ord(char) - ord('A')
            plain_idx = (idx * k_inv) % n
            plainChar = chr(plain_idx + ord('A'))
            plainText += plainChar
        else:
            plainText += char
            
    return plainText

def brute_force_multiplicative(cipherText):
    results = {}
    
    # Valid keys for n=26 are: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
    valid_keys = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

    for key in valid_keys:
        decrypted_text = multiplicative_decryption(cipherText, key)
        results[key] = decrypted_text
        print(f"Key K={key}: {decrypted_text}")
        
    return results
