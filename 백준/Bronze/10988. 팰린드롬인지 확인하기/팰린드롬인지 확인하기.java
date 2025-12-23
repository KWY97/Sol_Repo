import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        char[] arr = s.toCharArray();

        int left = 0;
        int right = arr.length - 1;
        int flag = 1;

        while (left < right) {
            if (arr[left] != arr[right]) {
                System.out.println(0);
                flag = 0;
                break;
            }
            left += 1;
            right -= 1;
        }

        if (flag == 1) {
            System.out.println(1);
        }
    }
}