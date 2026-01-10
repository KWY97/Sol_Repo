import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        double ans = Math.pow(2, n) + 1;
        ans = Math.pow(ans, 2);

        System.out.println((int) ans);
    }
}
