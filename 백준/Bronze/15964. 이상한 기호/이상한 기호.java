import java.util.Scanner;

public class Main {
    static long calculate(long a, long b) {
        long ans = (a + b) * (a - b);
        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long a = sc.nextLong();
        long b = sc.nextLong();

        System.out.println(calculate(a, b));
    }
}
