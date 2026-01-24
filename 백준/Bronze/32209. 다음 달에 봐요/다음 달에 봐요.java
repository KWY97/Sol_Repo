import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int q = sc.nextInt();
        int totalQ = 0;
        String ans = "See you next month";

        for (int i = 0; i < q; i++) {
            int n = sc.nextInt();
            int m = sc.nextInt();

            if (n == 1) {
                totalQ += m;
            } else {
                if (totalQ < m) {
                    ans = "Adios";
                    break;
                } else {
                    totalQ -= m;
                }
            }
        }
        System.out.println(ans);
    }
}
