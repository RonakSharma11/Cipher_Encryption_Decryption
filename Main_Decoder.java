import java.util.Scanner;

public class CaesarCipherDecoder {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the ciphertext: ");
        String ciphertext = scanner.nextLine();
        
        System.out.print("Enter the shift: ");
        int shift = scanner.nextInt();
        
        String plaintext = caesarCipherDecoder(ciphertext.toUpperCase(), shift);
        System.out.println("The plaintext is: " + plaintext);
        
        scanner.close();
    }
    
    public static String caesarCipherDecoder(String ciphertext, int shift) {
        StringBuilder plaintext = new StringBuilder();
        for (int i = 0; i < ciphertext.length(); i++) {
            char c = ciphertext.charAt(i);
            if (Character.isAlphabetic(c)) {
                // Convert the character to its ASCII code, then shift it back
                // by the specified amount, wrapping around if necessary
                int asciiCode = (int) c;
                int shiftedAsciiCode = (asciiCode - 'A' - shift + 26) % 26 + 'A';
                plaintext.append((char) shiftedAsciiCode);
            } else {
                plaintext.append(c);
            }
        }
        return plaintext.toString();
    }
}
