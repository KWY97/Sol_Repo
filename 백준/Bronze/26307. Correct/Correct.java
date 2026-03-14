import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int h = sc.nextInt();
        int m = sc.nextInt();

        int hSum = h - 9;

        System.out.println((hSum * 60) + m);
    }
}
