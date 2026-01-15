import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int apple = sc.nextInt() * 3;
        apple += sc.nextInt() * 2;
        apple += sc.nextInt();

        int banana = sc.nextInt() * 3;
        banana += sc.nextInt() * 2;
        banana += sc.nextInt();

        if (apple > banana) {
            System.out.println("A");
        } else if (apple < banana) {
            System.out.println("B");
        } else {
            System.out.println("T");
        }
    }
}
