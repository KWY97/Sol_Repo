import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        int result = 0;

        for (int i = 0; i < n; i++) {
            char[] word = sc.nextLine().toCharArray();
            result += check(word);
        }

        System.out.println(result);
    }

    public static int check(char[] word) {
        boolean[] used = new boolean[26];

        for (int i = 0; i < word.length; i++) {
            int idx = word[i] - 'a';

            if (used[idx]) {
                if (i > 0 && word[i-1] == word[i]) {
                    continue;
                } else {
                    return 0;
                }
            } else {
                used[idx] = true;
            }
        }
        return 1;
    }
}
