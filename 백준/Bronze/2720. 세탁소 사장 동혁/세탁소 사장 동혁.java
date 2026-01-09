import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            int c = scanner.nextInt();
            int q = 0;
            int d = 0;
            int n = 0;
            int p = 0;

            while (true) {
                // 탈출 조건
                if (c == 0) break;

                if (c >= 25) {
                    q += c / 25;
                    c %= 25;
                } else if (c >= 10) {
                    d += c / 10;
                    c %= 10;
                } else if (c >= 5) {
                    n += c / 5;
                    c %= 5;
                } else if (c >= 1) {
                    p += c / 1;
                    c %= 1;
                }
            }

            System.out.printf("%d %d %d %d", q, d, n, p);
            System.out.println();
        }
    }
}