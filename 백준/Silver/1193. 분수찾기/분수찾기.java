import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int position;
        int curNum = 1;
        int line = 1;

        while (true) {
            int maxNum = curNum + line - 1;

            if ((curNum <= n) && (n <= maxNum)) {
                position = n - curNum + 1;
                break;
            }

            curNum = maxNum + 1;
            line++;
        }

        // 홀수 라인 일 때
        if (line % 2 != 0) {
            // 분자
            int cnt = 0;
            for (int i = line; i > 0; i--) {
                cnt++;
                if (cnt == position) {
                    System.out.println(i + "/" + position);
                    break;
                }
            }
            // 분모 - 무조건 position
        } else {
            // 분자 - 무조건 position
            // 분모
            int cnt = 0;
            for (int i = line; i > 0; i--) {
                cnt++;
                if (cnt == position) {
                    System.out.println(position + "/" + i);
                    break;
                }
            }
        }
    }
}
