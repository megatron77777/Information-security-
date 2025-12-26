import string

def create_playfair_matrix(key):
    key = key.upper().replace(" ", "")
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    key_chars = []
    for char in key:
        if char not in key_chars and char != 'J':
            key_chars.append(char)
    
    for char in alphabet:
        if char not in key_chars:
            key_chars.append(char)
            
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(key_chars[i:i+5])
        
    return matrix

def preprocess_plaintext(plainText):
    plainText = plainText.upper()
    processed_text = ""
    
    for char in plainText:
        if 'A' <= char <= 'Z':
            if char == 'J':
                processed_text += 'I'
            else:
                processed_text += char
    
    final_digraphs = []
    i = 0
    while i < len(processed_text):
        char1 = processed_text[i]
        
        if i + 1 < len(processed_text):
            char2 = processed_text[i+1]
            
            if char1 == char2:
                final_digraphs.append(char1 + 'X')
                i += 1
            else:
                final_digraphs.append(char1 + char2)
                i += 2
        else:
            final_digraphs.append(char1 + 'X')
            i += 1
            
    return final_digraphs
