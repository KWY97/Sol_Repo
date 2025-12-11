import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int temp;

        int[] basket = new int[n];

        for (int i = 0; i < n; i++) {
            basket[i] = i + 1;
        }

        for (int i = 0; i < m; i++) {
            int basket1 = sc.nextInt();
            basket1 -= 1;
            int basket2 = sc.nextInt();
            basket2 -= 1;

            temp = basket[basket1];
            basket[basket1] = basket[basket2];
            basket[basket2] = temp;
        }

        for (int i = 0; i < n; i++) {
            if (i > 0) {
                System.out.print(" ");
            }
            System.out.print(basket[i]);
        }
    }
}