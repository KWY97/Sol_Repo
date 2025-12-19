import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < t; i++) {
            String s = sc.nextLine();
            char[] arr = s.toCharArray();

            System.out.print(arr[0]);
            System.out.println(arr[s.length()-1]);
        }
    }
}
