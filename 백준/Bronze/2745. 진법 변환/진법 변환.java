import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        char[] n = scanner.next().toCharArray();
        int b = scanner.nextInt();
        int ans = 0;

        String num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        
        int power = 1;
        for (int i = 0; i < n.length; i++) {
            int value = num.indexOf(n[i]);
            ans *= b;
            ans += value;
        }

        System.out.println(ans);
    }
}
