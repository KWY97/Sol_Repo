import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[8];
        char check = 'S';

        for (int i = 0; i < 8; i++) {
            arr[i] = sc.nextInt();
            if (arr[i] == 9) {
                check = 'F';
            }
        }
        System.out.println(check);
    }
}