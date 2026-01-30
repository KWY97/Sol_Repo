import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.nextLine();
        String targets = sc.nextLine();

        boolean[] check = new boolean[26];

        for (int i = 0; i < targets.length(); i++) {
            char c = targets.charAt(i);
            if (c != ' ') {
                check[c - 'A'] = true;
            }
        }

        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < a.length(); i++) {
            char cur = a.charAt(i);

            // 대문자이고, 바꿔야 하는 문자면 소문자로
            if (cur >= 'A' && cur <= 'Z' && check[cur - 'A']) {
                answer.append((char)(cur + ('a' - 'A')));
            } else {
                answer.append(cur);
            }
        }

        System.out.println(answer);
    }
}
