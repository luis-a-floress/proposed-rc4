from rc4 import rc4
from random import sample


def showStatus(process, plain_text, key, key_stream, crypt):
    print(process + " process:")
    print("[-] Plain text ->", plain_text)
    print("[-] Key ->", key)
    print("[-] Key Stream ->", key_stream)
    print("[-] " + process + " ->", crypt)


def main():
    plain_text = "meet me after the toga party"
    n = 8
    N = 2**n
    K = "hello world key"
    k = 4      # Key size in bytes
    secret_key = list(map(lambda x : ord(x), sample(K, k)))
    initial_vector = sample(range(N), k)
    # key = list(range(k))    # Key definition
    key = secret_key + initial_vector    # Key definition
    # S-boxes definition
    sbox = list(range(N))
    sboxes = [sbox[:N//2], sbox[N//2:]]

    # RC4 function call to encrypt
    encrypt, key_stream = rc4(key, k, plain_text, N, sboxes)

    # Show the encryption
    showStatus("Encryption", plain_text, key, key_stream, encrypt)

    # Reinitialize sboxes
    sboxes = [sbox[:N//2], sbox[N//2:]]
    # RC4 function call to decrypt
    decrypt, key_stream = rc4(key, k, encrypt, N, sboxes)
    # Show the decryption
    showStatus("Decryption", encrypt, key, key_stream, decrypt)
    
    

if __name__ == '__main__':
    main()