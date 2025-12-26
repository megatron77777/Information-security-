import string

def create_adfgvx_matrix(key):
    ADFGVX_CHARS = "ADFGVX"
    alphabet_full = string.ascii_uppercase + string.digits
    
    key = key.upper().replace(" ", "")
    
    matrix_chars = []
    for char in key:
        if char not in matrix_chars and char in alphabet_full:
            matrix_chars.append(char)
            
    for char in alphabet_full:
        if char not in matrix_chars:
            matrix_chars.append(char)
            
    matrix = {}
    for r in range(6):
        for c in range(6):
            char = matrix_chars[r * 6 + c]
            key_code = ADFGVX_CHARS[r] + ADFGVX_CHARS[c]
            matrix[char] = key_code
            
    return matrix

def adfgvx_substitution_encryption(plainText, matrix):
    substituted_text = ""
    
    processed_text = ""
    for char in plainText.upper():
        if char.isalnum():
            processed_text += char
    
    for char in processed_text:
        if char in matrix:
            substituted_text += matrix[char]
        else:
            substituted_text += char
            
    return substituted_text
