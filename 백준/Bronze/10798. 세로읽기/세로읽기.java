import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 5 * 15 배열 선언
        String[][] arr = new String[5][15];

        // 입력 받기
        for (int i = 0; i < 5; i++) {
            String line = scanner.nextLine();

            for (int j = 0; j < line.length(); j++) {
                arr[i][j] = String.valueOf(line.charAt(j));
            }
        }

        // 세로로 읽기
        for (int i = 0; i < 15; i++) {
            for (int j = 0; j < 5; j++) {
                if (arr[j][i] != null) {
                    System.out.print(arr[j][i]);
                }
            }
        }
    }
}
