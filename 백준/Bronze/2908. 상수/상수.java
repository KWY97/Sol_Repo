import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();

        char[] aArr = a.toCharArray();
        String reversedA = "";
        for (int i = aArr.length - 1; i >= 0; i--) {
            reversedA += aArr[i];
        }

        char[] bArr = b.toCharArray();
        String reversedB = "";
        for (int i = bArr.length - 1; i >= 0; i--) {
            reversedB += bArr[i];
        }

        int A = Integer.parseInt(reversedA);
        int B = Integer.parseInt(reversedB);

        if (A > B) {
            System.out.println(A);
        } else {
            System.out.println(B);
        }
    }
}
