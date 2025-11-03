import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int A;
        String B;
        Scanner sc = new Scanner(System.in);

        A = sc.nextInt();
        B = sc.next();

        for (int i = 2; i >= 0; i--) {
            int digit = B.charAt(i) - '0';
            System.out.println(A * digit);
        }
        System.out.println(A * Integer.parseInt(B));
    }
}