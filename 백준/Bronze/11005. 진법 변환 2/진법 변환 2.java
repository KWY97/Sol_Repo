import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int b = scanner.nextInt();

        String result = "";
        char[] num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();

        while (n >= b) {
            result += num[n % b];
            n /= b;
        }
        result += num[n];

        char[] ans = result.toCharArray();

        for (int i = ans.length - 1; i >= 0; i--) {
            System.out.print(ans[i]);
        }
    }
}