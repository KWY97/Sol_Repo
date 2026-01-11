import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int maxNum = 1;
        int cnt = 1;

        while (n > maxNum) {
            maxNum = maxNum + (6 * cnt);
            cnt ++;
        }
        System.out.println(cnt);
    }
}