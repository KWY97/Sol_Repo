import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int maxNum = -1000001;
        int minNum = 1000001;
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            int num1 = sc.nextInt();
            a[i] = num1;
        }

        for (int j = 0; j < n; j++) {
            int num2 = a[j];

            if (minNum > num2) {
                minNum = num2;
            }
            if (maxNum < num2) {
                maxNum = num2;
            }
        }

        System.out.print(minNum + " " + maxNum);
    }
}