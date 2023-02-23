#include <iostream>
#include <string>

using namespace std;

string caesarCipherDecoder(string ciphertext, int shift) {
    string plaintext = "";
    for (char c : ciphertext) {
        if (isalpha(c)) {
            // Convert the character to its ASCII code, then shift it back
            // by the specified amount, wrapping around if necessary
            int asciiCode = (int) c;
            int shiftedAsciiCode = (asciiCode - 'A' - shift + 26) % 26 + 'A';
            plaintext += (char) shiftedAsciiCode;
        } else {
            plaintext += c;
        }
    }
    return plaintext;
}

int main() {
    string ciphertext;
    int shift;

    cout << "Enter the ciphertext: ";
    getline(cin, ciphertext);

    cout << "Enter the shift: ";
    cin >> shift;

    string plaintext = caesarCipherDecoder(ciphertext, shift);

    cout << "The plaintext is: " << plaintext << endl;

    return 0;
}
