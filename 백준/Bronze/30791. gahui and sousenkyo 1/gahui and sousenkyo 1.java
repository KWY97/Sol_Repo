import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[5];
        for (int i = 0; i < 5; i++) {
            arr[i] = sc.nextInt();
        }
        sc.close();

        int sum = 0;
        for (int i = 1; i < 5; i++) {
            if ((arr[0] - arr[i]) <= 1000) {
                sum++;
            }
        }

        System.out.println(sum);
    }
}
