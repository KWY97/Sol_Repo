import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int n = 0;

        if (N % 4 == 0) {
            n = N / 4;
        } else {
            n = N / 4 + 1;
        }

        for (int i = 1; i <= n; i++) {
            System.out.print("long ");
        }
        System.out.println("int");
    }
}