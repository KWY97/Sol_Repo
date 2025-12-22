import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        char[] arr = s.toCharArray();
        int totalCount = 0;

        for (char c : arr) {
            int count = c;

            if (65 <= count && count <= 67) {
                totalCount += 3;
            } else if (68 <= count && count <= 70) {
                totalCount += 4;
            } else if (71 <= count && count <= 73) {
                totalCount += 5;
            } else if (74 <= count && count <= 76) {
                totalCount += 6;
            } else if (77 <= count && count <= 79) {
                totalCount += 7;
            } else if (80 <= count && count <= 83) {
                totalCount += 8;
            } else if (84 <= count && count <= 86) {
                totalCount += 9;
            } else if (87 <= count && count <= 90) {
                totalCount += 10;
            }
        }
        System.out.println(totalCount);
    }
}
