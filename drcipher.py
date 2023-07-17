key = "abcdefghijklmnopqrstuvwxyz"

def encrypt(n, plaintext):
    result =""
    for l in plaintext.lower():
        try:
            i =(key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n, ciphertext):
    result =""
    for l in ciphertext.lower():
        try:
            i =(key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

print("*** DR.CIPHER ***")
ans = input("Encrypt or Decrypt ?")
ans = ans.lower()
k = input ("Enter message: ")
nn = int(input("Enter number of rotation: "))
if ans == "encrypt":
    ret = encrypt(nn, k)
    print("Encrypted message: %s" % ret)
else:
    ret = decrypt(nn, k)
    print("Decrypted message: %s" % ret)
