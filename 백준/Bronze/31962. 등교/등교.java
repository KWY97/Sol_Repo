import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int x = sc.nextInt();
        int ans = -1;

        for (int i = 0; i < n; i++) {
            int s = sc.nextInt();
            int t = sc.nextInt();

            int arrivalTime = s + t;
            if (arrivalTime <= x) {
                ans = s;
            }
        }

        System.out.println(ans);
    }
}
