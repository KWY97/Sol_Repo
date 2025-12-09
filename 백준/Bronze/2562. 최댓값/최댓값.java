import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[9];
        int count = 0;
        int maxNum = 0;

        // 배열에 순서대로 입력 값 담기
        for (int i = 0; i < 9; i++) {
            arr[i] = sc.nextInt();
        }

        // 배열 순회하며 최대값과 번호 찾기
        for (int j = 0; j < 9; j++) {
            if (maxNum < arr[j]) {
                maxNum = arr[j];
                count = j + 1;
            }
        }

        System.out.println(maxNum);
        System.out.println(count);
    }
}