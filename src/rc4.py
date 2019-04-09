from ksa import ksa
from prga import prga


def rc4(key, k, plain_text, N, sboxes):
    # Shuffle the s-boxes
    sboxes = ksa(key[:k//2], key[k//2:], sboxes[0], sboxes[1], N)
    # Generates the key stream
    key_stream = prga(sboxes[0], sboxes[1], len(plain_text), N)
    # XOR a character and a key from the key stream to generate
    # the new encrypted text
    return "".join(map(lambda x, y: chr(ord(x)^y), plain_text, key_stream)), key_stream
