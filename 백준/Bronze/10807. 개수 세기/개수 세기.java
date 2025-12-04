import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
        int a[] = new int[count];
        int sum = 0;

        for (int i = 0; i < count; i++) {
            int n = sc.nextInt();
            a[i] = n;
        }

        int v = sc.nextInt();
        for (int i = 0; i < count; i++) {
            if (a[i] == v) {
                sum++;
            }
        }
        System.out.println(sum);
    }
}
