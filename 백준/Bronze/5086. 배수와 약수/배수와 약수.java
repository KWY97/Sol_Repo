import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int n = sc.nextInt();
            int m = sc.nextInt();

            if ((n == 0) && (m == 0)) {
                break;
            }

            String ans = "";
            if (m % n == 0) {
                ans = "factor";
            } else if (n % m == 0) {
                ans = "multiple";
            } else {
                ans = "neither";
            }

            System.out.println(ans);
        }
    }
}
