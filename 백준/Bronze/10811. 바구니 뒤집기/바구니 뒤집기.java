import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] basket = new int[n+1];

        for (int i = 0; i <= n; i++) {
            basket[i] = i;
        }

        for (int i = 0; i < m; i++) {
            int left = sc.nextInt();
            int right = sc.nextInt();

            while (left < right) {
                int temp = basket[left];
                basket[left] = basket[right];
                basket[right] = temp;
                left++;
                right--;
            }
        }

        for (int i = 1; i <= n; i++) {
            if (i > 1) {
                System.out.print(" ");
            }
            System.out.print(basket[i]);
        }
    }
}
