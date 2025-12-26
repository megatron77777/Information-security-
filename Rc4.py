def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S, length):
    i = 0
    j = 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]
        keystream.append(k)
    return keystream

def rc4_keystream(key, length):
    key_bytes = [ord(char) for char in key]
    S = KSA(key_bytes)
    return PRGA(S, length)


# اختبار المشتق الثنائي 


def binary_derivative_test(keystream_bits):
    n = len(keystream_bits)
    if n < 2:
        return {"passed": False, "message": "Keystream too short for derivative test."}

    derivative = []
    for i in range(n - 1):
        diff = keystream_bits[i] ^ keystream_bits[i+1]
        derivative.append(diff)

    from collections import Counter
    counts = Counter(derivative)
    zeros = counts.get(0, 0)
    ones = counts.get(1, 0)
    
    total = zeros + ones
    if total == 0:
        return {"passed": False, "message": "Derivative sequence is empty."}
        
    p_zeros = zeros / total
    
    is_balanced = (abs(p_zeros - 0.5) < 0.05)
    
    return {
        "passed": is_balanced,
        "derivative_length": total,
        "zeros_count": zeros,
        "ones_count": ones,
        "p_zeros": p_zeros,
        "message": "Passed (Balanced)" if is_balanced else "Failed (Imbalanced)"
    }


# اختبار نقط التغير 

def longest_run_test(keystream_bits):
    n = len(keystream_bits)
    if n == 0:
        return {"passed": False, "message": "Keystream is empty."}
        
    max_run_0 = 0
    max_run_1 = 0
    current_run = 0
    current_bit = -1
    
    for bit in keystream_bits:
        if bit == current_bit:
            current_run += 1
        else:
            if current_bit == 0:
                max_run_0 = max(max_run_0, current_run)
            elif current_bit == 1:
                max_run_1 = max(max_run_1, current_run)
            
            current_bit = bit
            current_run = 1
            
    if current_bit == 0:
        max_run_0 = max(max_run_0, current_run)
    elif current_bit == 1:
        max_run_1 = max(max_run_1, current_run)

    failure_threshold = max(8, int(n * 0.005))
    
    is_acceptable = (max_run_0 <= failure_threshold) and (max_run_1 <= failure_threshold)

    return {
        "passed": is_acceptable,
        "max_run_0": max_run_0,
        "max_run_1": max_run_1,
        "threshold": failure_threshold,
        "message": "Passed (Acceptable Run Lengths)" if is_acceptable else "Failed (Too Long Run)"
    }
