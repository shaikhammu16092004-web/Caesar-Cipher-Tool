# =========================================
# Caesar Cipher Tool
# Developed using Python
# =========================================


# Function for encryption and decryption
def caesar_cipher(text, shift, mode):

    result = ""

    # Convert shift to negative for decryption
    if mode == "decrypt":
        shift = -shift

    # Loop through each character
    for char in text:

        # Check if character is alphabet
        if char.isalpha():

            # Handle lowercase letters
            if char.islower():
                start = ord('a')

            # Handle uppercase letters
            else:
                start = ord('A')

            # Convert character into position number
            ascii_value = ord(char) - start

            # Shift character with wrap-around
            shifted_value = (ascii_value + shift) % 26

            # Convert back to character
            new_character = chr(shifted_value + start)

            # Add character to result
            result += new_character

        else:
            # Keep spaces and symbols unchanged
            result += char

    return result


# Main program loop
while True:

    print("\n====================================")
    print("       CAESAR CIPHER TOOL")
    print("====================================")

    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ")

    # Encrypt option
    if choice == "1":

        message = input("\nEnter your message: ")

        try:
            shift = int(input("Enter shift value: "))

            encrypted_text = caesar_cipher(message, shift, "encrypt")

            print("\nEncrypted Message:", encrypted_text)

        except ValueError:
            print("\n[!] Shift value must be a number.")

    # Decrypt option
    elif choice == "2":

        message = input("\nEnter your message: ")

        try:
            shift = int(input("Enter shift value: "))

            decrypted_text = caesar_cipher(message, shift, "decrypt")

            print("\nDecrypted Message:", decrypted_text)

        except ValueError:
            print("\n[!] Shift value must be a number.")

    # Exit option
    elif choice == "3":

        print("\nExiting Caesar Cipher Tool...")
        print("Thank you for using the program!")

        break

    # Invalid choice
    else:
        print("\n[!] Invalid choice. Please select 1, 2, or 3.")