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
    
    k_inv = mod_inverse(key, n)
    
    for char in cipherText:
        if 'A' <= char <= 'Z':
            idx = ord(char) - ord('A')
            plain_idx = (idx * k_inv) % n
            plainChar = chr(plain_idx + ord('A'))
            plainText += plainChar
        else:
            plainText += char
            
    return plainText
