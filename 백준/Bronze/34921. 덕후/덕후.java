import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int t = sc.nextInt();

        int ans = 10 + 2 * (25 - a + t);

        System.out.println(Math.max(ans, 0));
    }
}
