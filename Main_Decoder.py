def caesar_cipher_decoder(ciphertext, shift):
    """
    This program decrypts a caeser cipher with any requested shift.
    :param ciphertext:
    :param shift:
    :return:
    """
    plaintext = ""  # This holds the decrypted plaintext
    for c in ciphertext:  # This loops over each character in the ciphertext
        if c.isalpha():  # This makes sure that the character is an actual alphabetic letter
            # Convert the character to its ASCII code, then shift it back
            # by the specified amount, wrapping around if necessary
            ascii_code = ord(c)  # This gets the ASCII code of the character (ord is the function that converts into ASCII number)
            shifted_ascii_code = (ascii_code - ord('A') - shift) % 26 + ord('A')  # This results in the shifting of the ASCII code
            plaintext += chr(shifted_ascii_code)  # This converts the shifted ASCII to a character and adds to plaintext
        else:  # In the case of it not being a character
            plaintext += c  # This will add whatever the character was without modifying
    return plaintext  # This returns the decrypted plaintext

ciphertext = input("Enter the ciphertext: ")
shift = int(input("Enter the shift: "))

plaintext = caesar_cipher_decoder(ciphertext.upper(), shift)

print("The plaintext is:", plaintext)
