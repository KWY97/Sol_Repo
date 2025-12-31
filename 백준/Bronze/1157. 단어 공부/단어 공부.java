import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[] s = sc.nextLine().toUpperCase().toCharArray();
        int[] english = new int[26];

        for (int i = 0; i < s.length; i++) {
            int idx = s[i] - 'A';
            english[idx] += 1;
        }

        int max = 0;
        for (int i = 0; i < 26; i++) {
            max = Math.max(max, english[i]);
        }

        int count = 0;
        int idx = -1;

        for (int i = 0; i < 26; i++) {
            if (english[i] == max) {
                count++;
                idx = i;
            }
        }

        if (count != 1) {
            System.out.println('?');
        } else {
            System.out.println((char) (idx + 'A'));
        }
    }
}
