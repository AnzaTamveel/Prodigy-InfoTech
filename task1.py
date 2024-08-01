def get_position_in_alphabet(char):
    if char.isupper():
        return ord(char) - ord('A')  # Position for uppercase letters
    elif char.islower():
        return ord(char) - ord('a')  # Position for lowercase letters
    else:
        return -1  # Return -1 for non-alphabetic characters

def get_character_from_position(position, is_uppercase=True):
    if 0 <= position <= 25:
        if is_uppercase:
            return chr(position + ord('A'))  # For uppercase letters
        else:
            return chr(position + ord('a'))  # For lowercase letters
    else:
        return None  # Return None for invalid positions


print("1. Encryption")
print("2. Decryption")
Answer = ""
Choice = input("Enter your choice: ")
if Choice == "1":
    Plaintext = input("Enter plaintext: ")
    k = 3 
    for x in range(len(Plaintext)):
        p = get_position_in_alphabet(Plaintext[x])
        if p != -1:  # Only encrypt alphabetic characters
            c = (p + k) % 26
            is_upper = Plaintext[x].isupper()
            Answer += get_character_from_position(c, is_upper)
        else:
            Answer += Plaintext[x]  # Non-alphabetic characters are added as-is

    print("Encrypted text:", Answer)
elif Choice == "2":
    Ciphertext = input("Enter ciphertext: ")
    k = 3
    for x in range(len(Ciphertext)):
        p = get_position_in_alphabet(Ciphertext[x])
        if p != -1:  # Only decrypt alphabetic characters
            c = (p - k) % 26
            is_upper = Ciphertext[x].isupper()
            Answer += get_character_from_position(c, is_upper)
        else:
            Answer += Ciphertext[x]  # Non-alphabetic characters are added as-is

    print("Decrypted text:", Answer)
else:
    print("Invalid choice")
