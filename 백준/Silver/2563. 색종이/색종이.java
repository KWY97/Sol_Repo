import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 100 * 100 도화지
        int[][] board = new int[101][101];

        // 입력 받기
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            // 색종이 붙이기
            for (int j = x; j < x + 10; j++) {
                for (int k = y; k < y + 10; k++) {
                    board[j][k] += 1;
                }
            }
        }

        // 영역 구하기
        int result = 0;
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                if (board[i][j] == 0) {
                    continue;
                }
                result += 1;
            }
        }

        System.out.println(result);
    }
}
