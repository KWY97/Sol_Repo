import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        int n = sc.nextInt();
        int sum = 0;
        int min = 10000;

        for (int i = m; i <= n; i++) {
            int num = i;
            int cnt = 0;

            for (int j = 1; j <= i; j++) {
                if (num % j == 0) {
                    cnt++;
                }
            }

            if (cnt == 2) {
                sum += num;
                if (min > num) {
                    min = num;
                }
            }
        }

        if ((sum == 0) && (min == 10000)) {
            System.out.println(-1);
        } else {
            System.out.println(sum);
            System.out.println(min);
        }
    }
}
