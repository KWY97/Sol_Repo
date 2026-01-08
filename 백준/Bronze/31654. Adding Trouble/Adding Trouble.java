import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        System.out.println(check(a, b, c));

    }

    public static String check(int a, int b, int c) {
        if (a + b == c) return "correct!";
        return "wrong!";
    }
}