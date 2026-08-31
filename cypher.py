print("=" * 50)
print("HIT137 - Software Now - Assignment 2")
print("Group Name: DAN/EXT04")
print("=" * 50)
print("Group Members:")
print("_" * 50)
print(f"{'Amber Francis':<20} {'s403747':>20}")
print(f"{'Darren Bragg':<20} {'s406821':>20}")
print(f"{'Duncan Brown':<20} {'s407728':>20}")
print(f"{'Jonathan Falkner':<20} {'s400817':>20}")
print("_" * 50)
print(" " * 50)
print(" " * 50)
print(" " * 50)
print("_" * 50)
print("Question 1")
print("_" * 50)


def encrypt_file(char, shift1, shift2):
    if char.islower():
        index = ord(char) - ord('a')
        if index < 13:                                          # a-m
            new_index = (index + shift1 * shift2) % 13          # uses first half of alphabet for letter wrapping
        else:                                                   # n-z
            rel = index - 13
            new_index = 13 + (rel - shift1 - shift2) % 13       # uses second half of alphabet for letter wrapping
        return chr(new_index + ord('a'))
    elif char.isupper():
        index = ord(char) - ord('A')
        if index < 13:                                          # A-M
            new_index = (index - shift1) % 13                   # uses first half of alphabet for letter wrapping
        else:                                                   # N-Z
            rel = index - 13
            new_index = 13 + (rel + shift2 * shift2) % 13       # uses second half of alphabet for letter wrapping
        return chr(new_index + ord('A'))
    elif char.isdigit():
        return str((int(char) + shift1 - shift2) % 10)
    else:
        return char

def encode_text(text, shift1, shift2):
    result = ""
    for char in text:
        result += encrypt_file(char, shift1, shift2)
    return result

def decrypt_file(char, shift1, shift2):
    if char.islower():
        index = ord(char) - ord('a')
        if index < 13:                                          # a-m
            orig_index = (index - shift1 * shift2) % 13         # uses first half of alphabet for letter wrapping
        else:                                                   # n-z
            rel = index - 13
            orig_index = 13 + (rel + shift1 + shift2) % 13      # uses second half of alphabet for letter wrapping     
        return chr(orig_index + ord('a'))
    elif char.isupper():
        index = ord(char) - ord('A')
        if index < 13:                                          # A-M
            orig_index = (index + shift1) % 13                  # uses first half of alphabet for letter wrapping
        else:                                                   # N-Z
            rel = index - 13
            orig_index = 13 + (rel - shift2 * shift2) % 13      # uses second half of alphabet for letter wrapping
        return chr(orig_index + ord('A'))
    elif char.isdigit():
        return str((int(char) - shift1 + shift2) % 10)
    else:
        return char

def decode_text(text, shift1, shift2):
    result = ""
    for char in text:
        result += decrypt_file(char, shift1, shift2)
    return result

def main():
    input_file = "raw_text.txt"
    with open(input_file, "r") as file:
        content = file.read()
    shift1 = int(input("Enter the first letter shift value (+ve integer): "))
    shift2 = int(input("Enter the second letter shift value (+ve integer): "))

    # Encode the text and save to a file
    encoded = encode_text(content, shift1, shift2)
    encrypted_file = "encrypted_text.txt"
    with open(encrypted_file, "w") as file:
        file.write(f"{shift1}, {shift2}\n")
        file.write(encoded)
    print(f"Done! The encoded text was saved to {encrypted_file}")

    # Decode straight after
    decoded = decode_text(encoded, shift1, shift2)
    decrypted_file = "decrypted_text.txt"
    with open(decrypted_file, "w") as file:
        file.write(decoded)
    print(f"Done! The decoded text was saved to {decrypted_file}")

    # Compare original content to the decoded result
    if content == decoded:
        print("Woohoo! The decoded text matches the original.")
    else:
        print("Fail! The decoded text does NOT match the original.")



if __name__ == "__main__":
    main()
