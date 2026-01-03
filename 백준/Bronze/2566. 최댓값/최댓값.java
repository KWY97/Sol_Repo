import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 최대값 저장 변수
        int max = -1;
        // 최대값 i 인덱스 저장 변수
        int iMax = -1;
        // 최대값 j 인덱스 저장 변수
        int jMax = -1;

        // 9 * 9 크기 2차원 배열 생성
        int[][] arr = new int[9][9];

        // 입력 받기
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        // 최댓값 찾기 및 인덱스 업데이트
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (max < arr[i][j]) {
                    max = arr[i][j];
                    iMax = i + 1;
                    jMax = j + 1;
                }
            }
        }

        System.out.println(max);
        System.out.print(iMax + " " + jMax);
    }
}
