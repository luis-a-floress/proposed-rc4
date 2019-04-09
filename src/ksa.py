"""
    Function Key-Scheduling Alforithm

    is used to shuffle the s-boxes.
"""
def ksa(key1, key2, sbox1, sbox2, N):
    j = 0
    for i in range(N//2):
        # j actualization
        j = (j + sbox1[i] + key1[i % len(key1)]) % (N//2)
        # Swap values
        sbox1[i], sbox1[j] = sbox1[j], sbox1[i]
        # j actualization
        j = (j + sbox2[i] + key2[i % len(key2)]) % (N//2)
        # Swap values
        sbox2[i], sbox2[j] = sbox2[j], sbox2[i]

    return [sbox1, sbox2]