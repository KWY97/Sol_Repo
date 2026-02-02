import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        while (true) {
            int n = sc.nextInt();
            int sum = 0;
            String ans = "";

            if (n == -1) break;

            for (int i = 1; i < n; i++) {
                if (n % i == 0) {
                    sum += i;
                    ans += i + " + ";
                }
            }

            ans = ans.substring(0, ans.length() - 3);

            if (sum == n) {
                System.out.println(n + " = " + ans);
            } else {
                System.out.println(n + " is NOT perfect.");
            }
        }
    }
}
