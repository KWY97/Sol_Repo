import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        int total = 0;

        String s = sc.nextLine();
        char[] arr = s.toCharArray();

        for (char c : arr) {
            total += c - '0';
        }

        System.out.println(total);

    }
}
