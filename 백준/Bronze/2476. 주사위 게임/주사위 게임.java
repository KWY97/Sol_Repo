import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cnt = sc.nextInt();
        int ans = 0;

        for (int i = 0; i < cnt; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int price = 0;

            if ((a == b) && (b == c)) {
                price = 10000 + a * 1000;
            } else if ((a == b) || (b == c)) {
                price = 1000 + b * 100;
            } else if (a == c) {
                price = 1000 + a * 100;
            } else {
                int temp1 = Math.max(a, b);
                int temp2 = Math.max(b, c);
                price = (Math.max(temp1, temp2)) * 100;
            }

            if (ans < price) {
                ans = price;
            }
        }
        System.out.println(ans);
    }
}