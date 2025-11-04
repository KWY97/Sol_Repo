import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int cnt = 0;
        Scanner sc = new Scanner(System.in);

        while (sc.hasNextLine()) {
            String n = sc.nextLine();
            cnt += 1;
        }
        System.out.println(cnt);
    }
}