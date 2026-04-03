import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int l = 2 * n;
        int[] arr = new int[l];

        for (int i = 0; i < l; i++) {
            arr[i] = sc.nextInt();
        }

        int ans = 0;

        for (int i = 0; i < l-1; i++) {
            for (int j = i+1; j < l; j++) {
                if (arr[i] == arr[j]) {
                    if (ans < j - i - 1) {
                        ans = j - i - 1;
                    }
                    break;
                }
            }
        }
        System.out.println(ans);
    }
}