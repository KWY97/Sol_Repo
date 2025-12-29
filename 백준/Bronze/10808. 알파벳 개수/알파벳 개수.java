import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[] s = sc.nextLine().toCharArray();
        int[] e = new int[26];

        for (char c : s) {
            e[c - 'a'] += 1;
        }

        for (int i = 0; i < e.length; i++) {
            if (i != 0) {
                System.out.print(" ");
            }
            System.out.print(e[i]);
        }
    }
}
