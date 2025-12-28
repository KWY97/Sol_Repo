import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            int totalY = 0;
            int totalK = 0;

            for (int j = 0; j < 9; j++) {
                int y = scanner.nextInt();
                int k = scanner.nextInt();

                totalY += y;
                totalK += k;
            }

            if (totalY > totalK) {
                System.out.println("Yonsei");
            } else if (totalY < totalK) {
                System.out.println("Korea");
            } else {
                System.out.println("Draw");
            }
        }
    }
}
