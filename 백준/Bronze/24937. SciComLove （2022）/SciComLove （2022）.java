import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long n = sc.nextLong();

        String s = "SciComLove";
        int k = (int)(n % 10);

        String result = s.substring(k) + s.substring(0, k);
        System.out.println(result);
    }
}
