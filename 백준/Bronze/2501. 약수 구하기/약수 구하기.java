import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int p = sc.nextInt();
        int q = sc.nextInt();
        int cnt = 0;
        int ans = 0;

        for (int i = 1; i <= p; i++) {
            if (p % i == 0) {
                cnt++;

                if (cnt == q) {
                    ans = i;
                    break;
                }
            }
        }
        System.out.println(ans);
    }
}
