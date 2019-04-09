"""
    Function Pseudo Random Number Generation Algorithm

    generates the key stream to make XOR with the plain text.
"""
def prga(sbox1, sbox2, len_plain_text, N):
    i = j1 = j2 = x = 0
    key_stream = []
    while (i < len_plain_text):
        # j1 actualization
        j1 = (j1 + sbox1[i]) % (N//2)
        # Swap values
        sbox1[i], sbox2[j1] = sbox2[j1], sbox1[i]
        # key 1 obtained
        t1 = sbox1[(sbox1[i] + sbox1[j1]) % (N//2)] +1
        # j2 actualization
        j2 = (j2 + sbox2[i]) % (N//2)
        # Swap values
        sbox2[i], sbox1[j2] = sbox1[j2], sbox2[i]
        # key 2 obtained
        t2 = sbox2[(sbox2[i] + sbox2[j2]) % (N//2)] +1
        # Key XOR insertion in key stream
        key_stream.insert(x, (t1^t2) % N)
        # i actualization
        i = (i+1) % (N//2)
    return key_stream