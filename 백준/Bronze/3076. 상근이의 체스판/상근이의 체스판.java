import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int r = sc.nextInt();
        int c = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();

        int row = r * a;
        int col = c * b;

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < row; i++) {
            int originRow = i / a;

            for (int j = 0; j < col; j++) {
                int originCol = j / b;

                if ((originRow + originCol) % 2 == 0) sb.append('X');
                else sb.append('.');
            }
            sb.append('\n');
        }

        System.out.println(sb.toString());
    }
}