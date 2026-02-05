import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];
        int ans = 0;

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int num : arr) {
            int cnt = 0;

            for (int j = 1; j <= num; j++) {
                if (num % j == 0) {
                    cnt++;
                }
            }

            if (cnt == 2) {
                ans++;
            }
        }

        System.out.println(ans);
    }
}
