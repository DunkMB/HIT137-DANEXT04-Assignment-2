def cypher(char, shift1, shift2):
    if char.isupper():
        return chr((ord(char) - ord('A') + shift1 + shift2) % 13 + ord('A'))
    elif char.islower():
        return chr((ord(char) - ord('a') + shift1 * shift2) % 26 + ord('a'))
    else:
        return char  # leave numbers, spaces, punctuation unchanged

def encode_text(text):
    result = ""
    for char in text:
        if char.isupper():
            result += cypher(char, 2, 4)
        elif char.islower():
            result += cypher(char, 2, 4)
        else:
            result += char
    return result

def main():
    input_filename = input("Filename to read: ")
    with open(input_filename, "r") as file:
        content = file.read()
    shift1 = int(input("Enter the first shift value (+ve integer): "))
    shift2 = int(input("Enter the second shift value (+ve integer): "))
    encoded = encode_text(content)

    output_filename = "encoded_" + input_filename
    with open(output_filename, "w") as file:
        file.write(encoded)

    print(f"Done! Encoded text saved to {output_filename}")

if __name__ == "__main__":
    main()
