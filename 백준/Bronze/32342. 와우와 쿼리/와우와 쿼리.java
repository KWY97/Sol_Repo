import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int q = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < q; i++ ) {
            String s = sc.nextLine();
            int cnt = 0;

            for (int j = 0; j <= s.length() - 3; j++) {
                if (s.substring(j, j+3).equals("WOW")) {
                    cnt++;
                }
            }
            System.out.println(cnt);
        }
    }
}
