# Task 1

print()
print("-------------------- Welcome to Caesar Cipher Program --------------------")
print()


def encrypt(plaintext, key):
    cipher = ""
    for i in plaintext:
        if i.isalpha():
            i.lower()
            cipher_text = chr(ord(i) + key)
            if ord(cipher_text) > 122:
                cipher_text = chr(ord(cipher_text) - 26)
            cipher += cipher_text
        else:
            cipher += i
    print(f"Ciphertext is : {cipher}", end=" ")


def decrypt(ciphertext, key):
    plaintxt = ""
    for i in ciphertext:
        if i.isalpha():
            i.lower()
            plain_text = chr(ord(i) - key)
            if ord(plain_text) < 97:
                plain_text = chr(ord(plain_text) + 26)
            plaintxt += plain_text
        else:
            plaintxt += i
    print(f"Plaintext is : {plaintxt}", end=" ")


print("Please select Encryption or Decryption: ")
user_input = input("Encrypt / Decrypt: ").lower()
print()

if user_input == "encrypt":
    print("Enter plaintext: ")
    plain_text = input()
    print("Enter key substitution (from 1 to 26): ")
    key = int(input())
    encrypt(plain_text, key)

elif user_input == "decrypt":
    print("Enter ciphertext: ")
    cipher_text = input()
    print("Enter key substitution (from 1 to 26): ")
    key = int(input())
    decrypt(cipher_text, key)
