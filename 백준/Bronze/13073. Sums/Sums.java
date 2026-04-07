import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();

            int first = n * (n + 1) / 2;
            int second = n * n;          
            int third = n * n + n;       

            System.out.println(first + " " + second + " " + third);
        }

        sc.close();
    }
}