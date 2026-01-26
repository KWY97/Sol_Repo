import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int v = sc.nextInt();

        int x = (v - a) / (a - b);
        if ((v - a) % (a - b) != 0) {
            x++;
        }
        System.out.println(x + 1);
    }
}
